from odoo import fields,models

class EstatePlan(models.Model):
    _name = "estate.property"
    _description = "This is Estate property model"

    name = fields.Char(string='name',required=True)
    description = fields.Text(string='description')
    postcode = fields.Char(string='postcode',required=True)
    date_availability = fields.Date(string='date')
    expected_price = fields.Float(string='expected_price',required=True)
    selling_price = fields.Float(string='selling_price')
    bedrooms = fields.Integer(string='bedrooms')
    living_area = fields.Integer(string='living_area')
    facades = fields.Integer(string='facades')
    garage = fields.Boolean(string='garage')
    garden = fields.Boolean(string='garden')
    garden_area = fields.Integer(string='garden_area')
    garden_orientation = fields.Selection(
        string='garden_orientation',
        selection=[('north','North'),('south','South'),('east','East'),('west','West')]
    )
    