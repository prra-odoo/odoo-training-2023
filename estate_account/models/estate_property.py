from odoo import  models,Command

class EstateProperty(models.Model):
    _inherit ="real.estate.properties"

    def action_sold(self):
        # breakpoint()
        for record in self:
            self.env["account.move"].create(
            {
                "partner_id":record.buyer_id.id,
                "move_type":'out_invoice',
                "invoice_line_ids":[
                    Command.create({
                        'name':record.name,
                        'quantity':0.06,
                        'price_unit':record.selling_price   

                      }),
                    Command.create( {
                        'name':'Administrative fees',
                        'price_unit':100
                    })],
            }
        )
            return super().action_sold()