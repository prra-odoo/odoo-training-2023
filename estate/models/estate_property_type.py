from odoo import models, fields,api

class EstatePropertyType(models.Model):
    _name= "estate.property.type"
    _description = "this is a estate property module "
    _order = "sequence desc"
    _sql_constraints = [
        ("unique_name","UNIQUE(name)","A property type name must be unique"),
    ]

    name = fields.Char(required=True)
    property_ids = fields.One2many("estate.property","property_type_id")
    sequence = fields.Integer('Sequence',default=1)
    offer_ids = fields.One2many("estate.property.offer","property_type_id")

    # Computed fields
    offer_count = fields.Integer(compute="_compute_offer_count")

    # Compute Methods
    @api.depends("offer_ids")
    def _compute_offer_count(self):
        for record in self:
            record.offer_count = len(record.offer_ids)
        return True