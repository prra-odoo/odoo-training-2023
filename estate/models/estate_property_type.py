from odoo import models ,fields

class EstatePropertyType(models.Model):
    _name = 'estate.property.type'
    _description = "Real Estate Property Type"

    name = fields.Char(required=True)
    
    _sql_constraints = [
        ("unique_property_types","unique(name)","The property name must be unique")
    ] 


    