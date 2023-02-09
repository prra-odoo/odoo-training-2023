from odoo import models,fields

class EstatePropertyOffer(models.Model):
    
    _name = "estate.property.offer"
    _description = "Property Offer Model"

    price = fields.Float()
    status = fields.Selection(
        string="Property status",
        selection=[('accepted','Accepted'),('refused','Refused')],
        copy=False)
    partner_id = fields.Many2one("res.partner",string="partner",required=True)
    property_id = fields.Many2one("estate.property",required=True)