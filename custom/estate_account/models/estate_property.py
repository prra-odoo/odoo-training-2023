from odoo import api,fields, models

class EstateProperty(models.Model):
    # _description = "estate property"
    _inherit="estate.property"

    def action_sold(self):
        print("Hello")
        # breakpoint()
        self.env['account.move'].create({
                'partner_id':self.buyer.id,
                'move_type':'out_invoice'
            })
        return super().action_sold()