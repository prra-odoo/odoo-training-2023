from odoo import fields,models

class EstatePropertyOffer(models.Model):
    _name="estate.property.offer"
    _description="list of property offers"

    price = fields.Float()
    status = fields.Selection(
        string = "Status",
        selection = [('accepted','Accepted'),('refused','Refused')],
        help  = "Status of offers",
        copy = False
        )
    
    partner_id = fields.Many2one('res.partner',required=True)
    property_id = fields.Many2one('estate.property',required=True)
    