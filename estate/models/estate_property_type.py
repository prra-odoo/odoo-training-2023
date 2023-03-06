from odoo import api, models, fields


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Real Estate Property Type"

    name = fields.Char(required=True)
    sequence = fields.Integer(string="Sequence")
    _order = "sequence,name"
    property_ids = fields.One2many("estate.property", "property_type_id")
    offer_ids = fields.One2many("estate.property.offer", "property_type_id")
    offer_count = fields.Char(compute="_compute_offer_count")
    _sql_constraints = [
        ("unique_property_types", "unique(name)", "The property name must be unique")
    ]

    @api.depends("offer_ids")
    def _compute_offer_count(self):
        for rec in self:
            rec.offer_count = self.offer_ids.search_count([])
