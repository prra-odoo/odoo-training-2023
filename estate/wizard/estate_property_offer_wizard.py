# -*- coding: utf-8 -*-

from odoo import models, fields, api

class EstatePropertyOfferWizard(models.TransientModel):
    _name = 'estate.property.offer.wizard'
    _description = 'Property offer wizard'

    # action = fields.Selection([('change_period', 'Change Period'), ('change_account', 'Change Account')], required=True)
    name = fields.Char()