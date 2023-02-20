from odoo import fields,models

class EstatePropertyType(models.Model):
    _name="estate.property.type"
    _description="Estate Property Type"
    _order="name"
    name=fields.Char(required=True)


    _sql_constraints=[
        ('unique_type','unique(name)','The Property type must be unique')
    ]



    property_ids=fields.One2many('estate.property','property_type_id')