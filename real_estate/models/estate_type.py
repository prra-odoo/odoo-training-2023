from odoo import fields, models 

class propertyType(models.Model):
    _name="estate.property.type"
    _description = "property type model"

    name = fields.Char('Name')