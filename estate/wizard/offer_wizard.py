from odoo import models,fields,Command

class EstateOfferWizard(models.TransientModel):
    _name="estate.offer.wizard"
    _description="Estate Offer Wizard"

    price = fields.Float(required = True)
    buyer_id = fields.Many2one("res.partner",required = True)
    property_type_id = fields.Many2one("estate.property.type")

    def action_create_offer(self):
        properties = self.env["estate.property"].search([])
        for record in properties:
            if(record.property_type_id == self.property_type_id):
                self.env["estate.property.offer"].create({
                    'price': self.price,
                    'partner_id': self.buyer_id.id,
                    'property_id': record.id
                })