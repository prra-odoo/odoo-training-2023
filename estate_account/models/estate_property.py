from odoo import models, Command


class EstateAccount(models.Model):
    _inherit = 'estate.property'

    def action_sold_button_header(self):
        for rec in self:
            self.env['account.move'].check_access_rights('write')
            self.env['account.move'].check_access_rule('write')
            self.env['account.move'].sudo().create({
                "partner_id": rec.buyer_id.id,
                "move_type": "out_invoice",
                "invoice_line_ids": [(
                    0, 0,
                    {
                        "name": rec.name,
                        'price_unit': rec.selling_price + 100.0,
                        'quantity': 1,
                    }
                )]
                # 'invoice_line_ids': [
                #     Command.create({
                #         "name": rec.name,
                #         'price_unit': rec.selling_price,
                #         'quantity': 1,
                #     },
                #     {
                #         "name": "Administrative Fees",
                #         'price_unit': 100.0,
                #         'quantity': 1,
                #     })
                # ]
            })
        return super(EstateAccount, self).action_sold_button_header()
