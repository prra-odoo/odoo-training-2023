from odoo import models,fields

class Estate(models.Model):
    _name="real_estate.properties"
    _description="Property Model"

    name=fields.Char(string="Title",required=True)
    description=fields.Text('Description')
    postcode=fields.Char('Postcode')
    date_availability=fields.Date('Date Availabilty')
    expected_price=fields.Float('Expected Price',required=True)
    selling_price=fields.Float('Selling Price',required=True)
    bedrooms=fields.Integer('Bedrooms')
    living_area=fields.Integer('Living Area')
    facades=fields.Integer('Facades')
    garage=fields.Boolean('Garage')
    garden=fields.Boolean('Garden')
    garden_orientation=fields.Selection(selection=[('north','North'), ('south','South'), ('east','East'),('west','West')])