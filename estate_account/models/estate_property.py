from odoo import models,Command

class EstateProperty(models.Model):

    _inherit="estate.property"

    def action_sold(self):
            rslt=self.env['account.move'].create({
                'partner_id':self.buyer_id.id,
                'move_type':'out_invoice',
                'name':self.name,
                'line_ids':[
                  Command.create({
                    'quantity':1,
                    'price_unit':(self.selling_price*0.6)+100}),
                ]
            })
            return super(EstateProperty,self).action_sold()