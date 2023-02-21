from odoo import models,fields,_

class EstatePropertyTag(models.Model):
    _name='estate.property.tag'
    _description= 'Creating an many to many property tag '
    _order="name"

    name= fields.Char(required=True)
    color=fields.Integer()

    _sql_constraints=[('tags_name_unique','unique(name)',
        'Propert Tags name should be Unique.')]