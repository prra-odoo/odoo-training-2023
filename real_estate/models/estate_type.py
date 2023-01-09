from odoo import fields, models
 

class propertyType(models.Model):
    _name="estate.property.type"
    _description = "property type model"
    _order = "name"

    name = fields.Char('Name')
    property_ids = fields.One2many("estate.property", "property_type_id", string="Properties")
    sequence = fields.Integer("Sequence", default=3)
