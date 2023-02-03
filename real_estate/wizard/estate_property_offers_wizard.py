# -*- coding: utf-8 -*-

from odoo import models, fields

class EstatePropertyOffersWizard(models.TransientModel):
    _name = "estate.property.offers.wizard"
    _description = "On clicking wizard button, Offer will be add in all the selected properties." 
    
    price = fields.Float(string="Price")
    partner_id = fields.Many2one("res.partner", required=True)
    validity = fields.Integer(string="Validity (days)", default=7)
    date_deadline = fields.Date(string="Deadline", compute="_compute_date_deadline", inverse="_inverse_date_deadline")