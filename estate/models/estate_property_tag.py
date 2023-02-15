from odoo import models, fields


class EstatePropertyTag(models.Model):
    _name="estate.property.tag"
    _description="This is property tag model"

    name = fields.Char(string="Tag Name",required=True)    