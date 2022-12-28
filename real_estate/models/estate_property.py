# -- coding: utf-8 --

from odoo import fields, models

class estateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate model"

    name = fields.Char('Name :', required = True)
    description = fields.Text('Description ')
    postcode = fields.Char('Postcode ')
    date_availability = fields.Date(default=lambda self: fields.Datetime.now())
    expected_price = fields.Float()
    selling_price = fields.Float()
    bedrooms = fields.Integer('Bedrooms ')
    living_area = fields.Integer('Living Area ')
    facades = fields.Integer('Facades ')
    garage = fields.Boolean('Garage ')
    garden = fields.Boolean('Garden ')
    garden_area = fields.Integer('Garden Area ')
    garden_orientation = fields.Selection(string="Orientation ",
        selection=[('north', 'North'), ('south', 'South'), ('east','East'), ('west','West')],
        help="Type is used to separate Leads and Opportunities")
    state = fields.Selection(selection= [('new','New'),('confirm','Confirm'),('cancel','Cancel')], default="new")
    activate = fields.Boolean(default=True)
    property_type_id = fields.Many2one("estate.property.type",string= "Property type")
    salesman_id=fields.Many2one("res.users",string="salesman",default=lambda self: self.env.user)
    buyer_id = fields.Many2one("res.partner", string="Buyers")