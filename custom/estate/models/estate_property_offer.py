from odoo import models,fields
class EstatePropertyType(models.Model):
    _name = "estate.property.offer"
    _description = "Real Estate Property Offer"
    price=fields.Float()
    status=fields.Selection(string="select the status",
    selection=[("accepted","Accepted"),("refused","Refused")],
    help="select the status")
    property_id=fields.Many2one("estate.real.property")
    partner_id=fields.Many2one("res.partner")