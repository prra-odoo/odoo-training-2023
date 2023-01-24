from odoo import models,Command

class EstateProperty(models.Model):
    _inherit="real.estate.property"

    def action_state_sold(self):
        for record in self:
            
            self.env["account.move"].create({
                'move_type':'out_invoice',
                'partner_id': record.buyer_id.id,
                
                'invoice_line_ids':[
                    Command.create({
                        'name':record.name,
                        'quantity':0.06,
                        'price_unit':record.selling_price
                    }),
                    Command.create( {
                        'name':'Administrative fees',
                        'price_unit':100
                    })
                ],
            })
        return super().action_state_sold()
