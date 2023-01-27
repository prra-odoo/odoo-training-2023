# -*- coding: utf-8 -*-
from odoo import api, fields, models, Command, _
from odoo.exceptions import UserError
from datetime import date


class estateProperty(models.Model):
    _inherit = "estate.property"
    _description = "Inherit Estate Model"

    def action_sold(self):
        for rec in self:
            self.env['account.move'].check_access_rights('write')
            self.env['account.move'].check_access_rule('write')
            self.env['account.move'].sudo().create({
                'partner_id': rec.buyer_id.id,
                'invoice_date': date.today(),
                'move_type': 'out_invoice',
                'invoice_line_ids': [
                    Command.create({
                    "name": rec.name,
                    "quantity": 1.0,
                    "price_unit": rec.selling_price * 6.0 / 100.0,
                    # "tax_ids": False,
                },),
                    Command.create({
                        "name": 'Administrative Fees',
                        "quantity": 1.0,
                        "price_unit": 100,
                    })
                ]
            })

        return super().action_sold()
