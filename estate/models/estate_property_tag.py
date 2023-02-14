from odoo import models,fields

class EstatePropertyTag(models.Model):
    _name="estate.property.tag"
    _description = "Estate Property Tag"
    _sql_constraints = [
                    ('name', 'UNIQUE (name)', 'You can not have two tags with the same name !')
                ]

    name = fields.Char(required=True)

    

    

