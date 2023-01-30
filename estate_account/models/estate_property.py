# -*- coding: utf-8 -*-

from odoo import Command
from odoo import models
from datetime import date


class EstateProperty(models.Model):
    _inherit = "real.estate"

    def sold_button(self):
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
                    },),
                    Command.create({
                        "name": 'Administrative Fees',
                        "quantity": 1.0,
                        "price_unit": 100,
                    })
                ]
            })

  
