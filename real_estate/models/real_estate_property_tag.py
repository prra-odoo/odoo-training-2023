from odoo import models, fields

class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "This model will have the tags related to propterties!"


    name = fields.Char(required=True)