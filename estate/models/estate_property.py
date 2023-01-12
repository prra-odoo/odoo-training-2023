from odoo import models,fields

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Property Model"

    name = fields.Char(required=True)
    description = fields.Text('description')
    postcode = fields.Char('postcode')
    data_avabilability = fields.Date('Datetime')
    expected_price = fields.Float()
    selling_price = fields.Float()
    bedrooms = fields.Interger()
    living_area = fields.Interger()
    facades = fields.Interger()
    garage = fields.Boolean()
    garden_area = fields.Interger()
    garden_orientation = fields.Selection()