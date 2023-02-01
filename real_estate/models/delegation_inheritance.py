from odoo import models, fields

class Delegation(models.Model):
    _name = "delegation.inheritance"
    _inherits = {'estate.property': 'property_id'}

    property_id = fields.Many2one(comodel_name="estate.property")