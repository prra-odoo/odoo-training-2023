from odoo import models,fields,_

class EstatePropertyTag(models.Model):
    _name='estate.property.tag'
    _description= 'Creating an many to many property tag '

    name= fields.Char(required=True)

    _sql_constraints=[('tags_name_unique','unique(name)',
        'Propert Tags name should be Unique.')]