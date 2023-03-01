from odoo import models , fields

class EstateProperty(models.Model):
    _inherit="estate.property"


    def action_set_sold(self):
        # print("hello")
        # breakpoint()
        self.env['account.move'].create(
            {
            "partner_id":self.buyer.id,
            "move_type":"out_invoice"
            }
        )
        return super().action_set_sold()