from odoo import models,fields,Command

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property Account"
    _inherit = "estate.property"

    
    def action_sold(self):
      self.env["account.move"].create(
        {
            "partner_id":self.buyer_id.id,
            "move_type": "out_invoice",
            "line_ids": [
                (0,0, 
                 {   'name': self.name, 
                     'price_unit': self.selling_price * 0.06,
                     'quantity':1
                 }),
                 Command.create({
                       'name':'Administrative Fees',
                       'quantity':1,
                       'price_unit':100
                 })
                    ]

        }
    )
      return super().action_sold()