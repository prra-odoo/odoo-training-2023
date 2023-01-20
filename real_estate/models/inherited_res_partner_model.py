from odoo import models,fields

class InheritedResPartnerModel(models.Model):
    _inherit='res.partner'
    property_ids=fields.One2many("real.estate.property","buyer_id",domain=[('state','=','sold')])