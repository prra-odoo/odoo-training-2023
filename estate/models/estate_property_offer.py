from odoo import models,fields

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Real-estate property offer"


    price= fields.Float()
    status=fields.Selection(
        selection=[('accepted','Accepted','refused','Refused')]
    )
