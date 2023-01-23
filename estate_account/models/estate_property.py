# -*- coding: utf-8 -*-
from odoo import models,Command

class inherited_model(models.Model):
    _inherit='real.estate.properties'

    def action_sold(self):
        # print("....................................hello")
        self.env['account.move'].create(
            {

                'invoice_line_ids': [Command.create({
                                    
                })]
            }
        )
        return super().action_sold()