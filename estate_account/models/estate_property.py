# -*- coding: utf-8 -*-
from odoo import models,Command

class EstateProperty(models.Model):
    _inherit = "estate.property"

    def action_sold(self):
        vals = {'partner_id':self.buyer_id.id,
                'move_type':'out_invoice',
                'invoice_line_ids':[
                    Command.create({
                        "name": self.name,
                        "quantity":1,
                        "price_unit":self.selling_price*0.06
                    }),
                    Command.create({
                        "name":"admin fees",
                        "quantity":1,
                        "price_unit":100
                    })
                ]}
        self.env["account.move"].create(vals)
        return super(EstateProperty,self).action_sold()