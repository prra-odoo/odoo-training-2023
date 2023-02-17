from odoo import models, fields


class EstatePropertyTag(models.Model):
    _name="estate.property.tag"
    _description="This is property tag model"
    _sql_constraints = [
        ("check_tag_name", "UNIQUE(name)", "The name must be unique"),
    ]


    name = fields.Char(string="Tag Name",required=True)    