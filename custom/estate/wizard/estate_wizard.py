from odoo import models, fields, api
from odoo.exceptions import UserError



class EstateWizard(models.TransientModel):
    _name="estate.wizard"
    _description="show wizard of properties"

    price = fields.Float()
    status = fields.Selection(string='Status',
        selection=[('accepted', 'Accepted'), ('refused', 'Refused')],
        help="What's the Status!", copy=False)

    partner_id = fields.Many2one("res.partner", string="Partner", required=True )

    def test(self):
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


            

 