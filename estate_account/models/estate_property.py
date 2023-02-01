from odoo import fields, models, api
from odoo import Command

class InheritedEstateProperty(models.Model):
    _inherit = "estate.property"

    def sold_click(self):
        self.env['account.move'].check_access_rights('write')
        self.env['account.move'].check_access_rule('write')
        print(" reached ".center(100, '='))
        self.sudo().create_invoice()

        return super().sold_click()
        

    def create_invoice(self):

        for record in self:
            invoice = self.env['account.move'].create(
                {'partner_id': record.buyer_id.id, 
                'move_type': 'out_invoice',
                'invoice_line_ids' : [
                    Command.create(
                        {
                            'name': record.description,
                            'quantity': 1,
                            'price_unit': 0.06 * record.selling_price,
                        }
                    ),
                    Command.create(
                        {
                            'name': 'Administrative Fees',
                            'quantity': 1,
                            'price_unit': 100,
                        }
                    )
                ]
                }
            )

            # Task : To create a real estate project and assign a task to it
            # when user press send button
            # self.env['project.project'].create({
            #     'name': 'Real Estate Project',
            #     'task_ids':[
            #         Command.create(
            #             {
            #                 'name': record.name,
            #                 'priority': '1',
            #             }
            #         )
            #     ]
            # }            
            # )
            

        