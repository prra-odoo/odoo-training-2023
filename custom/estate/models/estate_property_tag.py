from odoo import fields, models

class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "estate property tag"
   
    name = fields.Char(required=True, string="Tag")
    color = fields.Integer()
    _order = "name"

    _sql_constraints = [
        ('tag_uniq',"UNIQUE(name)",'Property Tag Must be Unique')
    ]