from odoo import models,Command

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property Model"
    _inherit = 'estate.property'

    def action_sold(self):
        values = {'partner_id':self.buyer_id.id,'move_type':'out_invoice','invoice_line_ids':[
            Command.create({
                "name": self.name,
                "quantity":1,
                "price_unit":self.selling_price*0.06
            }),
            Command.create({
                "name":"administrative fees",
                "quantity":1,
                "price_unit":100.00
            })
        ]}
        self.env['account.move'].create(values)    
        return super().action_sold()