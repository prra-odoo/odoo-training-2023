# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models,fields

class EstateProperty(models.Model):
    _inherit = "estate.properties"

    def action_sold(self):
        print(super().action_sold())
        # for record in self:
        #     self.env['account.move'].create
        #     (
        #       {
        #         'partner_id' : record.buyer_id.id,
        #       'move_type' : 'out_invoice',
        #       }  
        #     )
        return super().action_sold()