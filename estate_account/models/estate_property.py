from odoo import fields, models, api

class EstateProperty(models.Model):
    _inherit="estate.property"

    def action_set_sold(self):
        vals={
            'partner_id':self.buyer.id,
            'move_type':'out_invoice',
            'invoice_line_ids':[
                fields.Command.create({
                    "name": self.name,
                    "quantity":1,
                    "price_unit":self.selling_price*0.06
                }),
                fields.Command.create({
                    "name": "admin fees",
                    "quantity":1,
                    "price_unit":100.00
                })
            ]
        }
        self.env["account.move"].create(vals)
        return super(EstateProperty,self).action_set_sold()