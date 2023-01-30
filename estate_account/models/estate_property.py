# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields,models,Command

class EstateProperty(models.Model):
    _inherit =  "estate.properties"

    def action_sold(self):
        for record in self:
            print(" reached ".center(100, '='))
            if self.env['account.move'].check_access_rights('write') and self.env['account.move'].check_access_rule('write'):
                self.env["account.move"].sudo().create(
                {
                    "partner_id": record.buyer_id.id,
                    "move_type": "out_invoice",
                    "invoice_line_ids": [
                        Command.create({
                        'name':record.name,
                        'quantity':0.06,
                        'price_unit':record.selling_price
                    }),
                    Command.create( {
                        'name':'Administrative fees',
                        'price_unit':100
                    })],
                }
            )
        return super().action_sold()