import time
from odoo import models,fields
from odoo.exceptions import UserError

class EstateProperty(models.Model):
    _inherit = "estate.property" 

    def sold_action(self):
        
            self.env['account.move'].create({
            'name': self.name,
            'move_type': 'out_invoice',
            'partner_id': self.buyer_id.id,
            'invoice_date':fields.Date.context_today(self),
            'invoice_line_ids':[
                (0, 0, {
                    'name': "6 of selling price",                                              
                    'price_unit': self.selling_price * 0.06,                         
                    'quantity': 1, 
                    'tax_ids':None 
                }),
                (0, 0, 
                        {
                        'name': 'Administrative Fees',
                        'price_unit': 100,
                        'quantity': 1,
                        'tax_ids':None
                        }
                    )
                ],
            })
            return super().sold_action()
        

        



                                                       