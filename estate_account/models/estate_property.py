from odoo import models,fields,Command

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property Account"
    _inherit = "estate.property"

    
    def action_sold(self):
      for record in self:
        self.env["account.move"].create(
        {
            "partner_id":record.buyer_id.id,
            "move_type": "out_invoice",
            "line_ids": [
                (0,0, 
                 {   'name': record.name, 
                     'price_unit': record.selling_price * 0.06,
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