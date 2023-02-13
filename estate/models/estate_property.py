from odoo import models,fields,api
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError

import odoo

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Real Estate Model"

    name = fields.Char(required=True, string="Title")
    description = fields.Text()
    postcode = fields.Char()
    last_seen = fields.Datetime("Last Seen", default=lambda self: fields.Datetime.now())
    date_availability = fields.Date(default=lambda self: fields.Datetime.now()+relativedelta(months=3),copy=False)
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True,copy=False)
    bedrooms = fields.Integer(default='2')
    living_area = fields.Integer(string="Living Area (sqm)")
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()   
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string='Garden Orientation',
        selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
        help="Select your direction!")
    active = fields.Boolean(default=True,required=True)
    state = fields.Selection(
        string='State',
        selection=[('new', 'New'), ('offer received', 'Offer Received'), 
        ('offer accepted', 'Offer Accepted'), ('sold', 'Sold'), ('cancelled', 'Cancelled')],
        help="What's the Status!",default="new",required=True,copy=False)

    property_type_id = fields.Many2one("estate.property.type", string="Property Type")
    salesman_id = fields.Many2one("res.partner", string="Salesman", default=lambda self: self.env.user)
    buyer_id = fields.Many2one("res.users", string="Buyer",copy=False)
    property_tag_ids = fields.Many2many("estate.property.tag", string="Tags")
    offer_ids = fields.One2many("estate.property.offer", "property_id")

    total_area = fields.Integer(compute="_total_area")
    @api.depends('living_area','garden_area')
    def _total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    best_offer = fields.Float(compute='_best_offer')
    @api.depends('offer_ids')
    def _best_offer(self):
        for record in self:
            if record.offer_ids:
                record.best_offer = max(record.offer_ids.mapped('price'))
            else:
               record.best_offer =  0.0

    @api.onchange('garden')
    def _onchange_garden(self):
        for record in self:
            if record.garden: 
                record.garden_area = 10
                record.garden_orientation = "north"
            else:
                record.garden_area = 0.0
                record.garden_orientation = False
    
    def action_sold(self):
        for record in self:
            if record.state == 'cancelled':
                raise UserError('A canceled property cannot be sold')
            else:
                record.state = 'sold'

    def action_cancel(self):
        for record in self:
            if record.state == 'sold':
                raise UserError('A sold property cannot be cancelled')
            else:
                record.state = 'cancelled'


