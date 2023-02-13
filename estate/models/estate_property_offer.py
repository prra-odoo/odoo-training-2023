from odoo import models, fields


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "This is an Estate Property offers Model"

    price = fields.Float(string="Price", required=True)
    status = fields.Selection(copy=False, selection=[
                              ("act", "Accepted!"), ("ref", "Refused!")])

    partner_id = fields.Many2one(
        comodel_name="res.partner", string="Partner", required=True)

    property_id = fields.Many2one(
        comodel_name="estate.property", string="Property", required=True)
