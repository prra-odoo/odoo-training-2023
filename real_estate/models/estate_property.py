from odoo import models,fields

class estate_property(models.Model):
    _name="estate.properties"
    _description="Real estate prperties"

    name=fields.Char('Property name',required=True)
    description=fields.Text('Property description')
    postcode=fields.Char('Postcode',required=True)
    date_availability=fields.Date('Date availability')
    expected_price=fields.Float('expected price',required=True)
    selling_price=fields.Float('selling price',required=True)
    bedrooms=fields.Integer('bedrooms')
    living_area=fields.Integer('living area')
    


