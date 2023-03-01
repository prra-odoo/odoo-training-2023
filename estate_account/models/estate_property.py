from odoo import models,fields,Command

class EstateProperty(models.Model):
    _inherit = "estate.property"

    def action_sold(self):
        print("===========================",self)
        account_move = self.env["account.move"].create({
            'partner_id' : self.buyer_id.id,
            'move_type' : 'out_invoice',
            'journal_id' : 1,
            'invoice_line_ids' : [
                Command.create({
                    'name' : 'Available house',
                    'quantity' : 1,
                    'price_unit' : self.expected_price*0.06
                }),
                Command.create({
                    'name' : 'Administrative Fees',
                    'quantity' : 1,
                    'price_unit' : 100
                })
            ]
        })
        return super().action_sold()
