from odoo import  models,Command

class EstateProperty(models.Model):
    _inherit ="real.estate.properties"

    def action_sold(self):
        # breakpoint()
        print(" reached ".center(100, '='))
        for record in self:
            if self.env["account.move"].check_access_rights('write') and self.env["account.move"].check_access_rule('write'):
        
                self.env["account.move"].sudo().create(
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