from odoo import models,fields,api

class OfferWizard(models.TransientModel):
    _name = "offer.wizard"
    _description = "It's a offer wizard model"

    price = fields.Float(default=1000)
    status = fields.Selection([
        ('accepted','Accepted'),
        ('refused','Refused')
    ],
    copy=False,
    )
    partner_id = fields.Many2one("res.partner",string="buyer")

    def test(self):
        breakpoint()
        selected_property_ids = self.env.context.get('active_ids')
        for x in selected_property_ids:
            self.env['estate.property.offer'].create(
                {
                'price':self.price,
                'status' : self.status,
                'partner_id' : self.partner_id.id,
                'property_id': x,
                }
            )
        return True
