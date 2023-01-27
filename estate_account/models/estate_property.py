from odoo import models,Command

class EstateProperty(models.Model):
    _inherit="real.estate.property"

    def action_state_sold(self):
        for record in self:
            self.env['real.estate.property'].check_access_rights("write")
            self.env['real.estate.property'].check_access_rule("write")
            self.check_access_rights("write")
            self.check_access_rule("write")
            self.env["account.move"].sudo().create({
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
