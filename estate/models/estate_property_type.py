from odoo import models,fields

class estatePropertyType(models.Model):
    _name="estate.property.type"
    _description="estate property type"

    name= fields.Char("Type" ,required=True)
    list_property = fields.One2many('estate.property','property_type_id', string = "All property")
