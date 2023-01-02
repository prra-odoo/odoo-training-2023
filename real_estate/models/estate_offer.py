from odoo import fields, models 

class propertyoffer(models.Model):
    _name="estate.property.offer"
    _description = "property offer model"

    price = fields.Float("Price")
    partner_id = fields.Many2one("res.partner" ,required=True)
    property_id = fields.Many2one("estate.property",required=True)
    status = fields.Selection(selection= [('accepted','Accepted'),('refused','Refused')])
