from odoo import models ,fields


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "this is the Property Type Model"
   
    name = fields.Char(required=True) 
    _sql_constraints=[
        ('check_type_name','UNIQUE(name)','The name must be unique')
    ]
