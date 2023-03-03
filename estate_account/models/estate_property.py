from odoo import fields,models,Command

class EstateProperty(models.Model):
    _inherit = "estate.property"


    def action_sold(self):
        # breakpoint()
        self.env['account.move'].create({
            # 'name':self.name,
            'partner_id' : self.buyers_id.id,
            'move_type' : 'out_invoice',

            'line_ids':[
            Command.create({
            'name':self.name,
            'quantity':1,
            'price_unit':self.selling_price * 0.6
            }),

            Command.create({
            'name':'administrative fees',
            'quantity':1,
            'price_unit':100
            })
          ]

        })

        
        return super(EstateProperty,self).action_sold()