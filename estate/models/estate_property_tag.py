from odoo import models,fields

class estatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Property tag"

    name = fields.Char(required = True)




    _sql_constraints = [
        (
            'check_property_tag_uniqueness' , 'unique(name)',
            "Property tag already exist in the database"

        )
    ]
    