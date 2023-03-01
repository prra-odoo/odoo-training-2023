from odoo import models,Command

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Account Model"
    _inherit = "estate.property"

    def action_sold(self):
        # print("hi")
        self.env['account.move'].check_access_rights('write')
        self.env['account.move'].check_access_rule('write')
        self.env['account.move'].create(
            {
                'partner_id': self.buyer_id.id,
                'move_type' : 'out_invoice',
                'invoice_line_ids' : [
                    Command.create({
                        'name' : self.name,
                        'quantity' : 1,
                        'price_unit' : 0.06*self.selling_price + 100
                    }),
                ]
            }
        )
        return super(EstateProperty,self).action_sold()