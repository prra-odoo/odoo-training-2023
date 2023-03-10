from odoo import models,fields,Command

class PropertiesOfferWizard(models.TransientModel):
    _name='properies.offer.wizard'
    _description='Properties Offer Wizard'
   

    price=fields.Float('Price')
    status=fields.Selection(string="status", selection=[('accepted','Accepted'),('refused','Refused')])
    partner_id = fields.Many2one('res.partner', string='Buyer')

    def make_offer(self):
        active_ids=self._context.get("active_ids")

        for property_id in active_ids:       
            property=self.env['estate.property'].browse(property_id)
            print(property.mapped('name'))

            property.write({
                    "offer_ids":[ 
                        Command.create({ 
                            "price":self.price,
                            "partner_id":self.partner_id.id,

                    })
                    ],
                })