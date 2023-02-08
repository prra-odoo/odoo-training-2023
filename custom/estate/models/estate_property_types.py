from odoo import models,fields 
class estate_property_types(models.Model):
    _name="estate.property.types"
    _description="types of properties"
    name=fields.Char(required=True)
      