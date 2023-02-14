from odoo import models,fields,api
from dateutil.relativedelta import relativedelta

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate property model"

    name = fields.Char(default="Unknown")
    last_seen = fields.Datetime("Last seen",default = lambda self : fields.Datetime().now())
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date("Available from",default = lambda self : fields.Date.today()+relativedelta(months=3))
    expected_price = fields.Float()
    selling_price = fields.Float()
    bedrooms = fields.Integer(default = 2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(selection=[("north","North"),("south","South"),("east","East"),("west","West")])
    active = fields.Boolean(default = False)
    status = fields.Selection(selection=[("new","New"),("offer received","Offer Received"),("offer accepted","Offer Accepted"),("sold","Sold"),("canceled","Canceled")],default = "New",copy = False)
    property_type_id = fields.Many2one("estate.property.type",string="Property Type")
    sales_person_id = fields.Many2one('res.users', string="Salesman",default = lambda self : self.env.user)
    buyer_id = fields.Many2one('res.partner', string="Buyer")
    tag_ids = fields.Many2many('estate.property.tag')
    offer_ids = fields.One2many('estate.property.offer','property_id')
    total_area = fields.Float(compute = "_compute_area")
    best_price = fields.Float(compute = "_compute_bestprice")

    @api.depends("living_area","garden_area")
    def _compute_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area
    @api.depends("offer_ids.price")

    def _compute_bestprice(self):
        for record in self:
            record.best_price = max(record.mapped('offer_ids.price'))
        
