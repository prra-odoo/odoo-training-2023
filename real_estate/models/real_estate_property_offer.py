from odoo import fields, models


class RealEstatePropertyOffer(models.Model):
    _name = "real.estate.property.offer"
    _description = "Property Offers"

    price = fields.Float(required=True)
    status = fields.Selection(
        [('accepted', 'Accepted'), ('refused', 'Refused'),], copy=False)

    partner_id = fields.Many2one(
        "res.partner", string="Partner", required=True)
    property_id = fields.Many2one(
        "real.estate.property", string="Property Name", required=True)
