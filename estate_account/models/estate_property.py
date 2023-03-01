from odoo import fields,models,Command

class EstateProperty(models.Model):
    _inherit = ['estate.property']

    def action_do_sold(self):
        
        self.env['account.move'].create({
            'move_type' : 'out_invoice',
            'partner_id' : self.buyer_id.id,
            'invoice_line_ids' :  [
                Command.create({
                    'name' : self.name,
                    'quantity' : 1,
                    'price_unit' : self.selling_price*0.06
                }),
                Command.create({
                    'name' : 'administrative fees',
                    'quantity' : 1,
                    'price_unit' : 100
                }),
            ]
        })
        return super(EstateProperty,self).action_do_sold()