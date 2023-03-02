from odoo import api, models,fields,Command

class EstateProperty(models.Model):
    # _name = "estate.property"
    # _description = "Estate Property"
    
    _inherit = "estate.property"
    
    
    def action_sold(self):
        for rec in self :
            self.env['account.move'].create(
                {
                    'partner_id' : rec.buyer_id.id,
                    'move_type' :  'out_invoice',
                    'invoice_line_ids' :[                       
                     Command.create (
                        {
                            'name':'house available',
                            'quantity':1,
                            'price_unit':0.06*rec.selling_price,
                        },
                    ),
                    Command.create (
                        {
                            'name':'admintrative fees',
                            'quantity':1,
                            'price_unit':100,
                        },
                    ),
                    ],
                }   
               
            )
        return super().action_sold()
        
    
    