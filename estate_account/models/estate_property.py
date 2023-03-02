from odoo import models, Command


class EstateProperty(models.Model):
    _inherit = "estate.property"

    def btn_sold(self):
        self.env['account.move'].create({
            'partner_id': self.buyer_id.id,
            'move_type': 'out_invoice',
            'invoice_line_ids': [
                Command.create({
                    'name': self.name,
                    'quantity': 1,
                    'price_unit': 0.6*self.selling_price
                }),
                Command.create({
                    'name': 'Administrative Fees',
                    'quantity': 1,
                    'price_unit': 100
                })
            ]
        })
        return super().btn_sold()
