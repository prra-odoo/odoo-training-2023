from odoo import fields,models

class estateProperty(models.Model):
    _name = "estate.property"
    _description="model description"

    name=fields.Char(string="Name",required=True,help="this is name")
    description=fields.Text(string="Description")
    # postcode=fields.Char(string="Pin Code")
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
    