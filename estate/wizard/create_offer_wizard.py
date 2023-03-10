from odoo import models, fields


class CreateOfferWizard(models.TransientModel):

    _name = "create.offer.wizard"
    _discription = "Creating Offers Through Wizards"

    def _default_properties(self):
        
    property_id = fields.Many2one(
        "estate.property", string="Properties", required=True, default="_default_properties"
    )

    price = fields.Char()
    partner_id = fields.Many2one("res.partner")
    # offer_ids = fields.Many2many("estate.property.offer", string="Offers")
