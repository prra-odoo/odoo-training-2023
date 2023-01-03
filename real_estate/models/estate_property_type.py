from odoo import fields, models

class estatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Estate Property Type Model"

    name = fields.Char('Name', required = True)
    details = fields.One2many('estate.property','property_type_id')