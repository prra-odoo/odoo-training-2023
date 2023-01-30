# -*- coding: utf-8 -*-
from odoo import models,Command
from datetime import date
class inherited_model(models.Model):

    _inherit=['real.estate.properties']
    def action_sold(self):
        # print("....................................hello")
        for record in self :
            print(" reached ".center(100, '='))
            self.env['account.move'].check_access_rights('write')
            self.env['account.move'].check_access_rule('write')
            self.env['account.move'].create(
                {
                    'partner_id' : record.buyer.id, 
                    'move_type' : 'out_invoice',
                    'invoice_date' : date.today(),
                    'invoice_line_ids': [                        
                        Command.create({
                            'name' : record.description,
                            'price_unit' : record.selling_price*0.06,
                            'quantity' : 1

                        }),
                        
                        Command.create({
                            'name' : "Administrative Fees",
                            'price_unit' : 100,
                            'quantity' : 1
                        })
                    ]
                }

            )
            
            
        return super().action_sold()