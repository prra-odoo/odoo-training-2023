from odoo import models,fields 
class EstatePropertyTypes(models.Model):
    _name="estate.property.types"
    _description="types of properties"
    _order="sequence,name"
    name=fields.Char(required=True)
    sequence=fields.Integer()  
    _sql_constraints=[
        ('unique_property_type','unique(name)','Type names must be unique !')
                     ]
    
    property_ids=fields.One2many('estate.property','property_type_id')
      
    