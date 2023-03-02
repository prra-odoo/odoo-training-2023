from odoo import models,Command

class EstateProperty(models.Model):
    _inherit = 'estate.property'

    def action_sold(self):
       self.env['account.move'].create({
            'move_type': 'out_invoice',
            'partner_id': self.buyer_id.id,
            'invoice_line_ids': [
           Command.create({
                'name': self.name,
                'price_unit': self.selling_price * 0.06,
                'quantity': 1,
            }),
            Command.create({
                'name': 'Administrative fees',
                'price_unit': 100,
                'quantity': 1,
            })]
       })
       return super().action_sold()