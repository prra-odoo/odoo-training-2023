# -*- coding: utf-8 -*-
from odoo import models,fields,api
from odoo.exceptions import UserError,ValidationError


class estate_property(models.Model):
    _name = 'estate.property'
    _inherit = 'estate.property'
    _description = "Real Estate Module"

    def action_sold(self):
        print("hellooooooo")
                 
        # breakpoint()
        self.env['account.move'].sudo().create(
            {
                'move_type':'out_invoice',
                'partner_id':self.buyer.id,
                'invoice_date':fields.Date.context_today(self),
                'invoice_line_ids': [
                    (0, 0,                                                              # CREATE= 0
                        {                                                               # UPDATE= 1
                        'name': self.name,                                              # DELETE= 2
                        'price_unit': self.selling_price,                        # UNLINK= 3
                        'quantity': 1, 
                        'tax_ids':None                                                 # LINK= 4
                        }                                                               # CLEAR= 5
                    ), 
                    (0, 0,                                                              # CREATE= 0
                        {                                                               # UPDATE= 1
                        'name': '6% of selling price',                                              # DELETE= 2
                        'price_unit': self.selling_price * 0.06,                        # UNLINK= 3
                        'quantity': 1, 
                        'tax_ids':None                                                 # LINK= 4
                        }                                                               # CLEAR= 5
                    ), 
                    (0, 0, 
                        {
                        'name': 'Administrative Fees',
                        'price_unit': 100,
                        'quantity': 1,
                        'tax_ids':None
                        }
                    )                                                                 # SET= 6
                ],
            })
        return super().action_sold()