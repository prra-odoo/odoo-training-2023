# -*- coding: utf-8 -*-

from odoo import Command
from odoo import models
from datetime import date


class EstateProperty(models.Model):
    _inherit = "real.estate"

    def sold_button(self):
        for rec in self:
            self.env['account.move'].create({
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

        #     project = self.env['project.project'].create({
        #         'name': rec.name,

        #     })
        #     task = self.env['project.task'].create({
        #         'name': rec.name,
        #         'project_id' : project.id 
        #     })
        # return super().sold_button()
