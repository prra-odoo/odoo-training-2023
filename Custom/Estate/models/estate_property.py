from odoo import models, fields
from dateutil.relativedelta import relativedelta

class TestModel(models.Model):
    _name="estate.property"
    _description = "Testing an Estate Module"

    name = fields.Char(required=True,default="Unknown")
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(copy=False,default= lambda self: fields.Datetime.now()+relativedelta(month=3))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True,copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string = 'Type',
        selection = [('north','North'), ('south','South'), ('east','East'), ('west','West')],
        help = 'Select one from Below ')
    state = fields.Selection(
        selection = [('new','New'), ('offer received', 'Offer Received'), ('offer accepted', 'Offer Accepted'),
                      ('sold', 'Sold'), ('canceled', 'Canceled')  ],
                      default='new')
    active = fields.Boolean(default=True)
    # Linking Others Modules
    property_type_ID= fields.Many2one('estate.property.type',string="estate_type_partner")
    buyer=fields.Many2one('res.partner')
    salesperson = fields.Many2one('res.users', default= lambda self : self.env.user)
    tag_ids = fields.Many2many('estate.property.tag', string="estate_tags")
    offer_ids = fields.One2many('estate.property.offer',"property_id")

