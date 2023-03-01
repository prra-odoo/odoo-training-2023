from odoo import models,fields,api,Command

class EstateProperty(models.Model):
    _inherit = "estate.property"

    def action_set_state_sold(self):
        partner_id = self.buyer_id.id
        move_type = "out_invoice"
        invoice_lines = [
            Command.create({
            'name': self.name,
            'quantity': 1,
            'price_unit': self.selling_price,
            }),
            Command.create({
            'name': 'axu',
            'quantity': 1,
            'price_unit': 100,
            })
        ]
        self.env['account.move'].create(
            {
            'partner_id':partner_id,
            'move_type':move_type,
            'invoice_line_ids': invoice_lines
            }
            )
        return super(EstateProperty,self).action_set_state_sold()