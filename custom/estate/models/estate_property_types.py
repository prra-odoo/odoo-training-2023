from odoo import models,fields 
class EstatePropertyTypes(models.Model):
    _name="estate.property.types"
    _description="types of properties"
    name=fields.Char(required=True)
    _sql_constraints=[
        ('unique_property_type','unique(name)','Type names must be unique !')
                     ]
      
    