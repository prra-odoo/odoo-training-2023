
from odoo import models,fields,api,Command

class EstateRealProperty(models.Model):
    _name="estate.real.property"
    _inherit="estate.real.property"
    
    def action_sold(self):
        
        self.env['account.move'].create({
            'move_type': 'out_invoice',
            'partner_id': self.buyer_id.id,
             "line_ids": [
                    Command.create(
                        {
                            "name": self.name,
                            "quantity": 1,
                            "price_unit":0.6*self.selling_price +100
                        },
                    ),
                ],
        })
        
        return super(EstateRealProperty,self).action_sold()
        
