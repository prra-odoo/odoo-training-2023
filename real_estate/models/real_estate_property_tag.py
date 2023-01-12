from odoo import models, fields

class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "This model will have the tags related to propterties!"


    name = fields.Char(required=True)


    # defining sql constraints so that user cannot set multiple tags with same name
    _sql_constraints = [
        (
            'check_unique_tag_name',
            'unique (name)',
            'This tag name already exists. Name of the tag must be unique!'
        )
    ]