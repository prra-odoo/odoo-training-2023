from odoo import models ,fields


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "this is the Property Type Model"
    _order="sequence , name"
   
    name = fields.Char(required=True) 
    _sql_constraints=[
        ("check_type_name","UNIQUE(name)","The name must be unique")
    ]
    property_ids=fields.One2many("estate.property" ,"property_type_id")
    sequence=fields.Integer(string="Sequence" ,  default=1)
