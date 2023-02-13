from odoo import fields,models

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "It's a Estate Property Offer"

    price = fields.Float()
    status  = fields.Selection([
        ('accepted','Accepted'),
        ('refused','Refused')
    ],
    copy=False,
    )
    partner_id = fields.Many2one("res.partner",string="buyer",required=True)
    property_id = fields.Many2one("estate.property",string="Property ID",required=True)