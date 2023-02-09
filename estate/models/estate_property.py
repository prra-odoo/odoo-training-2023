from odoo import models,fields
from odoo.tools.rendering_tools import relativedelta_proxy

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description='Real Estate Property'
    
    name = fields.Char(required=True)
    description = fields.Char()
    postcode = fields.Char()
    date_availability = fields.Date(copy = False,default = lambda self : fields.Date.today()+relativedelta_proxy(months=3))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True,copy= False)
    bedrooms = fields.Integer(default = 2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    active = fields.Boolean(default = True)
    state = fields.Selection(
        string="State",
        default="new",
        selection=[('new','New'),('offer received','Offer Received'),('offer accepted','Offer Accepted'),('sold','Sold'),('cancelled','Cancelled')]
    )
    garden_orientation = fields.Selection(
        string = "Type",
        selection = [('north','North'),('South','South'),('East','East'),('West','West'), ],
        help = "Choose the direction"
    )
    property_type_id = fields.Many2one("estate.property.type",string="Property Type")
    buyer = fields.Many2one("res.partner",string="Buyer",copy=False)
    salesperson = fields.Many2one("res.users",string="Salesman",default=lambda self: self.env.user)
    