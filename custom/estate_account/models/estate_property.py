from odoo import models,fields,Command
class EstateProperty(models.Model):
    _inherit = "estate.property"

    def sold_action(self):
        # breakpoint()
        self.env['account.move'].create({
            'move_type':'out_invoice',
            'partner_id':self.buyer_id.id,
            'invoice_date':fields.Date.today(),
            'line_ids': [
                    Command.create({
                       'name' : self.name,
                       'price_unit':self.selling_price*0.06,
                       'quantity':1,
                       'tax_ids':False
                    }),
                    Command.create({
                       'name' :"Administrative fees",
                       'price_unit':100,
                       'quantity':1,
                       'tax_ids':False
                    })]
        })
        return super(EstateProperty,self).sold_action()