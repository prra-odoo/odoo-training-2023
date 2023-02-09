from odoo import models,fields

class EstatePropertyOffer(models.Model):
    _name="estate.property.offer"
    _description = "Estate Property Type"

    price = fields.Float()
    status = fields.Selection(string='Status',
        selection=[('accepted', 'Accepted'), ('refused', 'Refused')],
        help="What's the Status!",default="new", copy=False)
    partner_id = fields.Many2one("res.partner", string="Partner", required=True)
    property_id = fields.Many2one("estate.property", string="Property", required=True)


    

    

