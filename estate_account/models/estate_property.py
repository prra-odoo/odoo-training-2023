# -*- coding: utf-8 -*-
from odoo import api, fields, models, Command, _
from odoo.exceptions import UserError
from datetime import date


class estateProperty(models.Model):
    _inherit = "estate.property"
    _description = "Inherit Estate Model"

    def action_sold(self):
        for rec in self:
            self.env['account.move'].create({
                'partner_id': rec.buyer_id.id,
                'invoice_date': date.today(),
                'move_type': 'out_invoice',
                'invoice_line_ids': [(0, 0, {
                    "name": rec.name,
                    "quantity": 1.0,
                    "price_unit": rec.selling_price * 6.0 / 100.0,
                },),
                    (
                    0, 0,
                    {
                        "name": 'administrative fees',
                        "quantity": 1.0,
                        "price_unit": 100,
                    })
                ]
            })

        return super().action_sold()
