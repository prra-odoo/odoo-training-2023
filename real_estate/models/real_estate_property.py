from odoo import api, fields, models
from datetime import datetime
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError,ValidationError
from odoo.tools import float_compare, float_is_zero
# six_months_after  = datetime.now() + relativedelta(months=2)


class RealEstateProperty(models.Model):
    _name = "real.estate.property"
    _description = "Property Model"
    _order = "id desc"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name = fields.Char(string="Name", required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(default=datetime.now() + relativedelta(months=3))
    # date_availability = fields.Date(copy=False)
    expected_price = fields.Float(required=True)
    # expected_price = fields.Float('Expected Price', index=True,required=True)
    selling_price = fields.Float()
    # selling_price = fields.Float(readonly=True,copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    tatal_area = fields.Float(compute="_compute_total_area")
    garden_area = fields.Integer(compute="_cpmpute_garden", readonly=False)
    garden_orientation = fields.Selection([('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')])
    active = fields.Boolean(default=True)
    state = fields.Selection([('new', 'New'), ('offer_received', 'Offer Received'), ('offer_accepted',
                             'Offer Accepted'), ('sold', 'Sold'), ('canceled', 'Canceled')], default='new', required=True, copy=False, tracking=True)
    property_type_id = fields.Many2one('real.estate.property.type', string='Property Type')
    salesperson_id = fields.Many2one("res.users", string="Salesman", default=lambda self: self.env.user)
    buyer_id = fields.Many2one("res.partner", string="Buyer", copy=False)
    tag_ids = fields.Many2many("real.estate.property.tags")
    offer_ids = fields.One2many("real.estate.property.offer", "property_id", string="Offers")
    best_price = fields.Float(compute="_compute_best_offer")


    @api.depends("living_area", "garden_area")
    def _compute_total_area(self):
        for record in self:
            record.tatal_area = record.living_area + record.garden_area

    @api.depends('offer_ids')
    def _compute_best_offer(self):
        # print(self)
        for record in self:
            record.offer_ids.property_id = self.id
            record.best_price=max(record.offer_ids.mapped('price'),default=0)

    @api.depends('garden')
    def _cpmpute_garden(self):
        for record in self:
            if record.garden == True:
                record.garden_area, record.garden_orientation = 10, 'north'
            else:
                record.garden_area, record.garden_orientation = 0, ''

    def action_sold_porperty(self):
        for record in self:
            if record.state == 'canceled':
                raise UserError("A sold property cannot be canceled")
            record.state = 'sold'

    def action_cancel_porperty(self):
        for record in self:
            if record.state == 'sold':
                raise UserError("A canceled property cannot be sold")
            record.state = 'canceled'
    
    
    @api.constrains('selling_price', 'expected_price')
    def _check_price_validation(self):
        for record in self:
            if (not float_is_zero(record.selling_price, precision_rounding=0.1)) and float_compare(record.selling_price, 90/100 * record.expected_price,precision_rounding=0.1) < 0:
                    raise ValidationError("selling price cannot be less than 90% of expected price")
    
    
    @api.ondelete(at_uninstall=True)
    def _unlink_if_state_new_or_canceled(self):
        for record in self:
            if record.state in ['offer_received', 'offer_accepted', 'sold']:
                raise UserError(('You cannot delete a property that is in %s state.',dict(self._fields['state']._description_selection(self.env)).get(record.state)))
            
    _sql_constraints = [('check_expected_price', 'CHECK(expected_price >= 0)', 'The expected_price of an proerty should be greater than 0'),
                        ('check_selling_price', 'CHECK(selling_price >= 0)', 'The selling_price of an proerty should be greater than 0')]
            
            
    # @api.onchange('garden')
    # def _onchange_garden(self):
    #     if self.garden == True:
    #         self.garden_area, self.garden_orientation = 10, 'north'
    #     else:
    #         self.garden_area, self.garden_orientation = 0, ''
    # @api.constrains('expected_price','offer_ids')
    # def check_price(self):
    #     for record in self:
            
    #         # if record.selling_price <= (record.expected_price * 0.9) and record.offer_ids :
    #         #     print(record.offer_ids)
    #             # raise ValidationError(('The Selling Price cannot be lower than 90% of the Expected Price.'))