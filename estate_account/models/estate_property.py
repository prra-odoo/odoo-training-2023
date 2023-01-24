# -*- coding: utf-8 -*-

from odoo import models,Command

class estateAccount(models.Model):
    _inherit = "estate.property"

    def sold_button(self):
       for record in self:
            self.env['account.move'].create(
                {
                    "partner_id": self.buyer_id.id,
                    "move_type": 'out_invoice',
                    "invoice_line_ids": [
                        Command.create(
                            {
                                "name": record.name,
                                "quantity": 1.0,
                                "price_unit": record.selling_price * 6.0 / 100,
                            }
                        ),

                        Command.create(
                            {
                                "name": "Administrative Fees",
                                "quantity": 1.0,
                                "price_unit": 100,
                            }
                        ),
                    ],
                }
            )  
            return super().sold_button()
