# -*- coding: utf-8 -*-
from odoo import models,Command

class Estate_Property(models.Model):
    _inherit = "estate.property"

    def action_sold(self):
        # breakpoint()
        self.env['account.move'].create(
            {
                'name':'Estate Property',
                'partner_id': self.buyer_id.id,
                'move_type': 'out_invoice',
                'invoice_line_ids' :[
                    Command.create({
                    "name": self.name,
                    "quantity": 1,
                    "price_unit": self.selling_price*6/100,
                }),
                Command.create({
                    "name":"Adminstrative fees",
                    "quantity":1,
                    "price_unit":100,
                })
            ],
            }
        )
        self.env['project.project'].create(
            {
                'name':'Cleaning',
                'partner_id':self.buyer_id.id,
                'task_ids': [
                    Command.create({
                        "name":self.name,
                    })  
                ]

            }
        )
        return super().action_sold()