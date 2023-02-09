from odoo import models,fields 
class EstatePropertyTypes(models.Model):
    _name="estate.property.types"
    _description="types of properties"
    name=fields.Char(required=True)
      