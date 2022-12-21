from odoo import models,fields

class estateProperty(models.Model):
    _name = "estate.property"
    
    _description = "This is the description for the estate property"


    name = fields.Char(required=True)
    id = fields.Integer(required=True)
    description = fields.Text(copy=False)
    postcode = fields.Char()
    date_availability = fields.Date()
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(required=True,readonly=True)
    bedrooms = fields.Integer(default=4)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string='Type',
        selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')]
    )

