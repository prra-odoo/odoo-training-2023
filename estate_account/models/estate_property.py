from odoo import fields,models,Command

class Inherited_estate_property(models.Model):
    _inherit="estate.property.model"

    name=fields.Char(required=True)

    def perform_sold(self):

        for record in self:
            self.env['account.move'].sudo().create({
                'move_type': 'out_invoice',
                'partner_id': record.buyer_id.id,
                'invoice_date': '2023-01-28',
                'name': 'Property Invoicing',
                'invoice_line_ids': [
                    Command.create({
                        'name': record.name,
                        'price_unit': (0.06*(record.selling_price)),
                        'quantity': 1,
                    }),
                    Command.create({
                        'name': 'Administration fees',
                        'price_unit': 100,
                        'quantity': 1,
                    }),
                ],
                # 'invoice_line_ids': [(0, 0, {
                    # 'name': record.name,
                    # 'price_unit': (0.06*(record.selling_price)),
                    # 'quantity': 1,
                # }), (0,0, {
                    # 'name': 'Administration fees',
                    # 'price_unit': 100,
                    # 'quantity': 1,
                # })],
            })
        return super().perform_sold()





