from odoo import models,Command

class estateAccountInvoice(models.Model):
    _inherit = "estate.property"

    def sold_product(self):
        self.env['account.move'].create(
            {
                'partner_id': self.buyer_id.id,
                'move_type': 'out_invoice',
                'line_ids': [ Command.create
                    (
                        {
                            'name' : self.name,
                            'quantity':1,
                            'price_unit':0.94*self.selling_price

                        }
                    ),
                    Command.create({
                        'name': self.name,
                        'quantity': 1,
                        'price_unit':100
                    
                    })
                    
                ]
               
            }
            
        )
         
        return super(estateAccountInvoice,self).sold_product()
    










    