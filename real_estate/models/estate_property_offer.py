from odoo import models,fields

class estate_Property_offer(models.Model):
      _name = "estate.property.offer"
      _description = "Real estate based advertisedment module for the property type"

      price = fields.Float()
      status = fields.Selection(string='status',selection=[('Accepted','accepted'),('Refused','refused'),copy=False])
      partner_id = fields.Many2one("res.partner", string="Partner", required=True)
      property_id = fields.Many2one('estate.property',string="property id")


