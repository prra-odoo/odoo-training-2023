from odoo import fields,models

class Users(models.Model):
    _inherit = "res.users"
    _inherits = {'estate.property': 'property_ids'}

    property_ids = fields.One2many("estate.property","user_id", string = "Properties", domain = "[('state','in',('new','Offer Received'))]")
    test = fields.Char(string="test")
