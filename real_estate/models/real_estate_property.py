from odoo import models,fields,api,_
from odoo.exceptions import UserError,ValidationError
from odoo.tools.float_utils import float_is_zero,float_compare
from dateutil.relativedelta import relativedelta
class RealEstateProperty(models.Model):
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
    state=fields.Selection(selection=[('new','New'), ('offer_received','Offer Received'), ('offer_accepted','Offer Accepted'), ('sold','Sold'),('canceled','Canceled')],default='new')
    buyer_id = fields.Many2one("res.partner", string="Buyer")
    salesman_id=fields.Many2one("res.users",string="Salesman")
    type_id=fields.Many2one("real.estate.property.type",string="Property Type")
    tags_ids=fields.Many2many("real.estate.property.tags")
    offers_ids=fields.One2many("real.estate.property.offer","property_id",string="Offers")
    total_area=fields.Integer(compute="_compute_total_area",inverse="_inverse_total_area")
    best_offer=fields.Float(compute="_compute_best_offer")
    _sql_constraints=[('expected_price_positive','CHECK(expected_price>0)','Expected Price must be strictly positive'),('selling_price_positive','CHECK(selling_price>=0)','Selling price must be positive')]    
    @api.constrains("selling_price","expected_price")
    def _check_selling_price(self):
        for record in self:
            if float_compare(record.selling_price,record.expected_price*90/100,precision_digits=2)<0 and not float_is_zero(record.expected_price,precision_digits=2):
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
                if record.state in ('new',):
                    record.state='offer_received'
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