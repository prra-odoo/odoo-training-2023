from odoo import api, models, fields


class AddOfferWizard(models.TransientModel):
    _name = 'add.offer.wizard'
    _description = "Add Offer Wizard"


    # adding fields
    # These fields will be temporary and will be deleted periodically

    offer_price = fields.Float(required=True)
    partner_buyer_id = fields.Many2one(comodel_name="res.partner")
    sales_person_id = fields.Many2one(comodel_name="res.users")

    def _get_default_properties(self):
        return self.env['estate.property'].browse(self.env.context.get('active_ids'))
        
    property_ids = fields.Many2many("estate.property", default=_get_default_properties)

    def add_offer_function(self):
        for record in self:
            print(f"offer_price: {record.offer_price}")
            if record.property_ids:
                for property in record.property_ids:
                    self.env['estate.property.offer'].create({
                        'price': record.offer_price,
                        'partner_id': record.partner_buyer_id.id,
                        'property_id': property.id,
                    })