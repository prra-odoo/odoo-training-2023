# -*- coding: utf-8 -*-

from odoo import models, fields
from odoo.exceptions import UserError

class EstatePropertyAccount(models.Model):
    _inherit = "estate.property"
    
    test = fields.Char(string="Testing", help="This field is for testing purpose.")
    
    def action_sold_btn(self):
                
        # if self.env['account.move'].check_access_rights('write'):
        #     raise UserError('You do not have write access on Invoicing!!!')
        
        # Create invoice record, When property was sold.
        
            
        estate_invoice = self.env['account.move'].sudo().create([
            {   
                'move_type': 'out_invoice',
                'partner_id': self.buyer_id.id,
                'invoice_line_ids': [
                    (0, 0,                                                              # CREATE= 0
                        {                                                               # UPDATE= 1
                        'name': self.name,                                              # DELETE= 2
                        'price_unit': self.selling_price * 0.06,                        # UNLINK= 3
                        'quantity': 1,                                                  # LINK= 4
                        }                                                               # CLEAR= 5
                    ),                                                                  # SET= 6                 
                    (0, 0, 
                        {                            
                        'name': 'Administrative Fees',
                        'price_unit': 100,
                        'quantity': 1,
                        }
                    )
                ],
            }
        ])
        estate_invoice.action_post()
        
        return super().action_sold_btn()
