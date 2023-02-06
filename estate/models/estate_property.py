from odoo import models, fields

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "estate_property Model"

    name = fields.Char()
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date()
    expected_price = fields.Float()
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    living_area= fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    log_access = True
    garden_orientation = fields.Selection(
        string = 'Garden Orientattion',
        selection = [('north','North'),('south','South'),
                     ('east','East'),('west','West')],
    )
    