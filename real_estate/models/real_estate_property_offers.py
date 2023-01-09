from odoo import models, fields

class EstatePropertyOffers(models.Model):
    _name = "estate.property.offer"
    _description = "This model will contain estate property all the offers, price, status etc."

    price = fields.Float()
    status = fields.Selection([('accepted', 'Accepted'), ('refused', 'Refused')], copy=False)

    partner_id = fields.Many2one("res.partner", required=True)
    property_id = fields.Many2one("estate.property", required=True)