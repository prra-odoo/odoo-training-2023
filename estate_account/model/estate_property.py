# -*- coding: utf-8 -*-

from odoo import models, fields

class EstateProperty(models.Model):
    _inherit = "estate.property"

    def property_sold(self):
        for record in self:
            invoice_1 = self.env['account.move'].create({
                'move_type': 'out_invoice',
                'partner_id': record.buyer_id.id,
            })
        return super().property_sold

    # invoice_1 = self.env['account.move'].create({
    #         'move_type': 'out_invoice',
    #         'invoice_date': '2017-01-01',
    #         'date': '2017-01-01',
    #         'partner_id': self.partner_a.id,
    #         'currency_id': self.currency_data['currency'].id,
    #         'invoice_line_ids': [(0, 0, {
    #             'name': 'test line',
    #             'price_unit': 0.025,
    #             'quantity': 1,
    #             'account_id': self.company_data['default_account_revenue'].id,
    #         })],
    #     })
    # move_id 
    # partner_id