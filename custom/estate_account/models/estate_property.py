from odoo import api,fields, models,Command

class EstateProperty(models.Model):
    # _description = "estate property"
    _inherit="estate.property"

    def action_sold(self):
        print("Hello")
        # breakpoint()
        # for record in self:
        self.env['account.move'].create({
                "name":self.name,
                'partner_id':self.buyer.id,
                'move_type':'out_invoice',
                "line_ids": [
                Command.create({
                    "name": self.name,
                    "price_unit": self.selling_price*0.06,
                    "quantity":1.0
                }),
                Command.create({
                    "price_unit": 100,
                })   
            ]
            })
        return super().action_sold()