from odoo import models,fields,api,exceptions
from dateutil.relativedelta import relativedelta

class EstateProperty(models.Model):
    
    _name = "estate.property"
    _description = "Real Estate Model"

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    #date_availability = fields.Date(default=fields.Datetime.today())
    date_availability = fields.Date(default=lambda self: fields.Datetime.now()+relativedelta(months=3),copy=False,string="Available from")
    #if date is used then Date.today() and if Datetime is used then Datetime.now()
    last_seen = fields.Datetime("Last Seen", default=lambda self: fields.Datetime.now())
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True,copy=False)
    bedrooms = fields.Integer(default="2")
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    active = fields.Boolean(default=True)
    state = fields.Selection(
        string='state',
        selection=[('new', 'New'), ('offer accepted', 'Offer Accepted'), ('offer recieved', 'Offer Recieved'), ('sold', 'Sold'),('cancelled','Cancelled')],
        help="Select your state!",
        required=True,
        default="new",
        copy=False
        )
    garden_orientation = fields.Selection(
        string='Direction',
        selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
        help="Select your direction!"
        )
    property_type_id = fields.Many2one("estate.property.type", string="Property Type")
    buyer_id = fields.Many2one('res.partner',string="Buyer",copy=False)
    seller_id = fields.Many2one('res.users',string="Seller", default=lambda self: self.env.user)
    tag_ids = fields.Many2many("estate.property.tag",string="Property Tag")
    offer_ids = fields.One2many("estate.property.offer", "property_id")
    total_area = fields.Integer()
    
    total_area = fields.Integer(compute="_total_area",store=True)
    @api.depends('living_area','garden_area')
    def _total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    best_offer = fields.Float(compute='_best_offer',store=True)
    @api.depends("offer_ids")
    def _best_offer(self):
        for record in self:
            if(record.offer_ids):
                record.best_offer=max(record.offer_ids.mapped("price"))
            else:
                record.best_offer=0.0
    # onchange function when garden field is enabled
    @api.onchange('garden')
    def onchange_garden(self):
        for record in self:
            if record.garden:
                record.garden_area = 10.0
                record.garden_orientation = 'north'
            else:
                record.garden_area = 0.0
                record.garden_orientation = False
            
    #function making two button of sold and cancelled in header
    def action_cancel(self):
        for record in self:
            if record.state == 'sold':
                raise exceptions.UserError("sold property can't be cancelled.")
            else:record.state = 'cancelled'
    def action_sold(self):
        for record in self:
            if record.state == 'cancelled':
                raise exceptions.UserError("cancelled property can't be sold.")
            else: record.state = 'sold'

        