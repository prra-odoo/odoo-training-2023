from odoo import fields, models 

class propertytag(models.Model):
    _name="estate.property.tag"
    _description = "property tag model"

    name = fields.Char('Name')