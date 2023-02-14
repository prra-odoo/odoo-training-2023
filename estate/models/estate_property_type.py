from odoo import models,fields

class EstatePropertyType(models.Model):
    _name="estate.property.type"
    _description = "Estate Property Type"
    _sql_constraints = [
                    ('name', 'UNIQUE (name)', 'You can not have two properties with the same name !')
                ]

    name = fields.Char(required=True)

    
    

    

