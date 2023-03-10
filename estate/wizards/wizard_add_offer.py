from odoo import fields,models

class WizardAddOffer(models.TransientModel):
    _name = "wizard.add.offer"
    _description = "Add Offer Wizard"
    
    price = fields.Float()
    status = fields.Selection(string='Status',
        selection=[('accepted', 'Accepted'), ('refused', 'Refused')],
        help="What's the Status!", copy=False)
    partner_id = fields.Many2one("res.partner", string="Partner", required=True )

    # offer_ids = fields.One2many("estate.property.offer","property_id")

    def make_an_offer(self):
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