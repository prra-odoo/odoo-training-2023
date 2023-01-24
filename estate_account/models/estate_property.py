from odoo import models, Command


class EstateAccount(models.Model):
    _inherit = 'estate.property'

    def action_sold_button_header(self):
        for rec in self:
            self.env['account.move'].create({
                "partner_id": rec.buyer_id.id,
                "move_type": "out_invoice",
                # "invoice_date": rec.date_availability,
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
            print("-----------------------------------------")
            sid = self.env['project.project'].create({
                'name':rec.name
            })

            self.env['project.task'].create({
                'name':rec.name,
                'project_id' : sid.id
            })
        return super(EstateAccount, self).action_sold_button_header()
