from odoo import models,fields
from datetime import date

class EstateOffers(models.Model):
    _name= 'estate.property.offer'
    _description = 'Offer to estate property'

    price = fields.Float()
    status = fields.Selection(
        string= "Status",
        selection= [('accepted','Accepted'),('refused','Refused')],
        copy= False)
    partner_id = fields.Many2one('res.partner',required=True)
    property_id = fields.Many2one('estate.property',required=True)
    validity = fields.Integer(default=7)
    date_deadline= fields.Date()

    # @api.depends('date_deadline')
    # def _inverse_validity(self):
    #     today = date.today()
    #     for record in self:
    #         record.validity = record.