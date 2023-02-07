from odoo import models,fields,api,_,Command
from odoo.exceptions import UserError,ValidationError
from odoo.tools.float_utils import float_is_zero,float_compare
from dateutil.relativedelta import relativedelta
from odoo.addons.http_routing.models.ir_http import slug

class RealEstateProperty(models.Model):
    _inherit = ['mail.thread', 'mail.activity.mixin','website.published.multi.mixin','website.searchable.mixin',]
    _name='real.estate.property'
    _description="Property model"
    _order="id desc"
    name=fields.Char(string='Property Name',required=True)
    description=fields.Text()
    postcode=fields.Char()
    date_availability=fields.Date(default=fields.Datetime.now()+relativedelta(months=3))
    expected_price=fields.Float(required=True)
    selling_price=fields.Float()
    bedrooms=fields.Integer()
    living_area=fields.Integer()
    facades=fields.Integer()
    garage=fields.Boolean()
    garden=fields.Boolean()
    garden_area=fields.Integer(compute='_compute_garden',store=True,readonly=False)
    garden_orientation=fields.Selection(selection=[('north','North'),('south','South'),('east','East'),('west','West')])
    active=fields.Boolean(default=True)
    state=fields.Selection(selection=[('new','New'), ('offer_received','Offer Received'), ('offer_accepted','Offer Accepted'), ('sold','Sold'),('canceled','Canceled')],default='new',tracking=True)
    buyer_id = fields.Many2one("res.partner", string="Buyer")
    salesman_id=fields.Many2one("res.users",string="Salesman")
    type_id=fields.Many2one("real.estate.property.type",string="Property Type")
    tags_ids=fields.Many2many("real.estate.property.tags")
    offers_ids=fields.One2many("real.estate.property.offer","property_id",string="Offers")
    total_area=fields.Integer(compute="_compute_total_area",inverse="_inverse_total_area")
    best_offer=fields.Float(compute="_compute_best_offer")
    company_id=fields.Many2one('res.company', required=True, default=lambda self: self.env.company)
    image=fields.Binary()
    _sql_constraints=[('expected_price_positive','CHECK(expected_price>0)','Expected Price must be strictly positive'),('selling_price_positive','CHECK(selling_price>=0)','Selling price must be positive')]    
    @api.constrains("selling_price","expected_price")
    def _check_selling_price(self):
        for record in self:
            if self.offers_ids and float_compare(record.selling_price,record.expected_price*90/100,precision_digits=2)<0 and not float_is_zero(record.expected_price,precision_digits=2):
                raise ValidationError(_("the selling price cannot be lower than 90% of the expected price."))
    
    def action_state_sold(self):
        for record in self:
            if record.state=='canceled':
                raise UserError(_("A canceled property cannot be set as sold"))
            record.state='sold'
    def action_state_canceled(self):
        for record in self:
            if record.state=='sold':
                raise UserError(_("A sold property cannot be set as canceled"))
            record.state='canceled'
    def action_wizard_add_offer(self):
        wizard = self.env['real.estate.offers2property'].create({
                    'property_ids': [Command.set(self.ids)],
                })
        return {
                'type': 'ir.actions.act_window',
                'res_model': 'real.estate.offers2property',
                'view_type': 'form',
                'view_mode': 'form',
                'res_id': wizard.id,
                'target': 'new',
            }
    @api.depends("living_area","garden_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area=record.living_area+record.garden_area
    def _inverse_total_area(self):
        for record in self:
            record.living_area=record.total_area-record.garden_area
    @api.depends("offers_ids")
    def _compute_best_offer(self):
        for record in self:
            offer=record.offers_ids.mapped('price')
            if offer:
                record.best_offer=max(offer)
            else:
                record.best_offer=0
    @api.depends("garden")
    def _compute_garden(self):
        for record in self:
            if record.garden:
                record.garden_area=10
                record.garden_orientation='north'
            else:
                record.garden_area=0
                record.garden_orientation=''
    @api.ondelete(at_uninstall=False)
    def _delete_check_state(self):
        for record in self:
            if record.state not in ('new','canceled'):
                raise UserError(_("Only Properties in New and Canceled state can be deleted"))
    @api.depends('name')
    def _compute_website_url(self):
        super()._compute_website_url()
        for property in self:
            if property.id:  # avoid to perform a slug on a not yet saved record in case of an onchange.
                property.website_url = '/estate/{}'.format(slug(property))

   