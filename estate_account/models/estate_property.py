from odoo import models , fields , Command

class EstateProperty(models.Model):
    _inherit="estate.property"


    def action_set_sold(self):
        # print("hello")
        # breakpoint()
            self.env['account.move'].create(
                {
                'name':self.name,
                'partner_id':self.buyer.id,
                'move_type':'out_invoice',
                'invoice_line_ids':[
                    Command.create({
                'name':self.name,
                'quantity':1.0,
                'price_unit':self.selling_price*6.0/100.0,
                    }),
                    Command.create({
                'name':self.name,
                'quantity':1.0,
                'price_unit':100.0
                    })
                ]
                }
            )
            return super().action_set_sold()