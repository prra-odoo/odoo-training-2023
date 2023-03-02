from odoo import api, models, fields


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "This is a PropertyType model"
    _order = "name"

    _sql_constraints = [("type_uniq", "UNIQUE (name)",
                         "The type must be different from already defined types."),
                        ("type_notnull", "CHECK (name IS NOT NULL)",
                         "Property type cannot be NULL"),]

    name = fields.Char(string="Property Type")

    property_ids = fields.One2many(
        comodel_name="estate.property", inverse_name="property_type_id")

    sequence = fields.Integer(
        default=1, help="Used to order stages.", string="Sequence")

    offer_ids = fields.One2many(
        comodel_name="estate.property.offer", inverse_name="property_type_id")

    offer_count = fields.Integer(compute="_compute_total_offers")

    def _compute_total_offers(self):
        # obj = self.env['estate.property.offer']
        # print(obj.property_type_id, "----------")
        count = self.env['estate.property.offer'].search_count(
            domain=[("property_type_id", "=", self.id)])
        # The property_type_id is the field in estate_property_offer,
        # which links offers to a particular property type,
        # we simply compare the id of this particular type with the ids in
        # that table.

        # EstatePropertyType
        # house - type id - 1
        # villa - type id - 2
        # apartment - type id - 3

        # EstatePropertyOffer
        # offer1 -> type id - 1
        # offer2 -> type id - 1
        # offer3 -> type id - 2
        # offer4 -> type id - 2

        # total offers
        # type - id(1) - 2
        # type - id(2) - 2
        # type - id(3) - 0
        self.offer_count = count
