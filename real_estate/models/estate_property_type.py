from odoo import fields,models

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Estate Properties"

    name = fields.Char(required=True)

    #property type name must be unique
    _sql_constraints = [
        ('property_type', 'unique(name)', 'Property Type Is Already Available.')
    ]

    property_ids = fields.One2many("estate.model.line", "model_id")

    class EstateTypeLine(models.Model):
        _name = "estate.model.line"
        _description = "estate Model Line"

        model_id = fields.Many2one("estate.property.type")
        name = fields.Char()
        expected_price = fields.Integer()
        status = fields.Char()

