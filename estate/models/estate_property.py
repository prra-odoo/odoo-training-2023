from odoo import fields,models

class estate_property(models.Model):
    _name = "estate.property"
    _description = "estate property model"

    name=fields.Char(string="Name",required=True,help="this is name")
    description=fields.Text(string="Description")
    postcode=fields.Char(string="Pin Code",required=True)
    date_availability=fields.Date(string="Availablity Date")
    expected_price=fields.Float(string="Expected Price",required=True)
    selling_price=fields.Float(string="Selling Price")
    bedrooms=fields.Integer(string="Bedroom Number")
    living_area=fields.Integer(string="Living Area")
    facades=fields.Integer(string="Facades")
    garage=fields.Boolean(string="Garage")
    garden=fields.Boolean(string="Garden")
    garden_area=fields.Integer(string="Garden Area")
    garden_orientation=fields.Selection(
        string="Garden Orientation",
        selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')])
