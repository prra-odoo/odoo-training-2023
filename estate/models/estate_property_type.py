from odoo import fields,models

class EstatePropertyType(models.Model):
    _name="estate.property.type"
    _description="Estate Property Type"
    name=fields.Char(required=True)


    _sql_constraints=[
        ('unique_type','unique(name)','The Property type must be unique')
    ]