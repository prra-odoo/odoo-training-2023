from odoo import models,fields,api
from dateutil.relativedelta import relativedelta
# from odoo import api
from odoo.exceptions import UserError

class EstateWizard(models.TransientModel):
      _name = "estate.wizard"

      # offer_ids= fields.One2many('estate.property.offer','property_id')

      
      price = fields.Float(string="Price")
      partner_id = fields.Many2one("res.partner", required=True)

      def offers(self):
        active_ids=self._context.get('active_ids')
        for record in active_ids:
            property_id=self.env['estate.property'].browse(record)
            property_id.write({
                "offer_ids":[
                    fields.Command.create({
                        "price" : self.price,
                        "partner_id" : self.partner_id.id,
                    })
                ]
            })
        return True
