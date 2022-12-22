# -- coding: utf-8 --

from odoo import fields, models

class realEstate(models.Model):
    _name = "estate.model"
    _description = "Estate model"

    name = fields.Char('Name :', required = True)
    description = fields.Text('Description :')
    postcode = fields.Char('Postcode :')
    date_availability = fields.Date(default=lambda self: fields.Datetime.now())
    expected_price = fields.Float()
    selling_price = fields.Float()
    bedrooms = fields.Integer('Bedrooms :')
    living_area = fields.Integer('Living Area :')
    facades = fields.Integer('Facades :')
    garage = fields.Boolean('Garage :')
    garden = fields.Boolean('Garden :')
    garden_area = fields.Integer('Garden Area :')
    garden_orientation = fields.Selection(string="Orientation :",
        selection=[('north', 'North'), ('south', 'South'), ('east','East'), ('west','West')],
        help="Type is used to separate Leads and Opportunities")