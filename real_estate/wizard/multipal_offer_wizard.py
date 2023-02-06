# -*- coding: utf-8 -*-
from odoo import api,fields,models,Command
from dateutil.relativedelta import relativedelta

class multipal_offer(models.TransientModel):
    
    _name="multipal.offer.wizard"
    _description="Make multipal offers"
    
    price = fields.Float(string="Price")
    partner_id = fields.Many2one("res.partner", required=True)

    def Multipal_offers(self):
        active_ids=self._context.get('active_ids')
        for record in active_ids:
            property_id=self.env['real.estate.properties'].browse(record)
            property_id.write({
                "offer_ids":[
                    Command.create({
                        "price" : self.price,
                        "partner_id" : self.partner_id.id,
                    })
                ]
            })
        return True

     