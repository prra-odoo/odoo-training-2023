from odoo import models, Command


class EstateAccount(models.Model):
    _inherit = 'estate.property'

    def action_sold_button_header(self):
        id = ""
        domain = ['property_id.offer_ids', '=', self.id]
        records = self.env['estate.property.offer'].search([domain])
        for rec in records:
            if rec.status == "accepted":
                id = rec.id
        # selling_price = self.selling_price  + self.selling_price*0.06
        for rec in self:
            self.env['account.move'].create({
                "partner_id": rec.buyer_id.id,
                "move_type": "out_invoice",
                # "invoice_date": rec.date_availability,
                # "invoice_line_ids": [(
                #     0, 0,
                #     {
                #         "name": rec.name,
                #         'price_unit': rec.selling_price + 100.0,
                #         'quantity': 1,
                #     }
                # )],
                'line_ids': [
                    Command.create({
                        "name": rec.name,
                        'price_unit': rec.selling_price,
                        'quantity': 1,
                    })
                ]
            })
        return super(EstateAccount, self).action_sold_button_header()
