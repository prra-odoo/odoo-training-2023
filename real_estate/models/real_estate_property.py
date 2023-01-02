from odoo import models,fields

class property(models.Model):
    _name='real_estate.property'
    _description="Property model"
    name=fields.Char(string='Property Name',required=True)
    description=fields.Text()
    postcode=fields.Char()
    date_availability=fields.Date()
    expected_price=fields.Float(required=True)
    selling_price=fields.Float()
    bedrooms=fields.Integer()
    living_area=fields.Integer()
    facades=fields.Integer()
    garage=fields.Boolean()
    garden=fields.Boolean()
    garden_area=fields.Integer()
    garden_orientation=fields.Selection(selection=[('north','North'),('south','South'),('east','East'),('west','West')])