# -*- coding: utf-8 -*-
from odoo import models,Command


class EstateProperty(models.Model):
    _inherit = "estate.property"

    def sold_action(self):
        for record in self:
            # print('overwrite successfully')

            self.env["account.move"].create({
                'partner_id': record.buyer_id.id,
                'move_type':  'out_invoice',
                'invoice_line_ids': [
                    Command.create({
                    "name": record.name,
                    "quantity": 1.0,
                    "price_unit":record.selling_price*6.0/100,
                },),
                    Command.create({
                        "name": 'administrative fees',
                        "quantity": 1.0,
                        "price_unit":100,
                    })
                ]
            })
        return super().sold_action()

   