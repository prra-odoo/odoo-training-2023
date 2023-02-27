from odoo import models, fields, api


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Estate property type model"
    _order = "name"

    name = fields.Char(required=True)
    sequence = fields.Integer("Sequence", default=1)
    property_ids = fields.One2many("estate.property", "property_type_id")
    offer_ids = fields.One2many("estate.property.offer", "property_type_id")
    offer_count = fields.Integer(default=0, compute="_compute_offer_count")

    _sql_constraints = [
        ("unique_name", "UNIQUE(name)", "Tag names must be unique!")
    ]

    def action_do(self):
        print("==================", self.offer_count)

    @api.depends("offer_ids")
    def _compute_offer_count(self):
        for record in self.offer_ids:
            self.offer_count = len(self.offer_ids)
        print("==================", self.offer_count)
