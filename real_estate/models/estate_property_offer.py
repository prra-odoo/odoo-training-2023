from odoo import models,fields

class EstateOfferProperty(models.Model):
    _name="real.estate.property.offer"
    _description="Property Offer Model"

    name=fields.Char(string="name",required=True)
    price=fields.Float(string="Price")
    status=fields.Selection(string="status", selection=[('accepted','Accepted'),('refused','Refused')],copy=False)
    partner_id=fields.Many2one('res.partner',required=True)
    property_id=fields.Many2one('real.estate.properties',required=True)
    