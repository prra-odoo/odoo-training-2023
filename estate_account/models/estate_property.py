# -*- coding: utf-8 -*-
from odoo import models


class estate_property(models.Model):

    _inherit = "estate.property"

    def action_sold(self):
        res = super().action_sold()
        for property in self:
            self.env['account.move'].create(
                {
                    "partner_id": property.buyer_id.id,
                    "move_type": "out_invoice",
                    "invoice_line_ids": [
                        (0,0,{"name": property.name,"quantity": 1.0,"price_unit": property.selling_price *.06,'tax_ids':None },),
                        (0,0,{"name": "Administrative fees","quantity": 1.0,"price_unit": 100.0,},),
                    ],
                }
            )     
            self.env['project.project'].create(
                {
                    'name': self.name,
                    'task_ids': [(0, 0, {'name': "Cleaning",}),]
                }
            )           
        return res      