from odoo import models,fields

class EstatePropertyOffer(models.Model):
    _name="estate.property.offer"
    _description="Real Estate Property Offers"

    price=fields.Float()
    status=fields.Selection(
        copy=False,
        selection=[('accepted','Accepted'),('refused','Refused')]
    )
    partner_id=fields.Many2one("res.partner",string="Partner", required=True)
    property_id=fields.Many2one("estate.property",string="Property Id", required=True)
    