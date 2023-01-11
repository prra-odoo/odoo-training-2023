from odoo import fields, models

class estatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Estate Property Tag Model"
    _order = "name"

    name = fields.Char('Name', required = True)
    color = fields.Integer('Color', default=2)


    _sql_constraints = [
            ('name_uniq', 'unique (name)', "Tag name already exists !"),
    ]