from odoo import fields, models


class InheritedModel(models.Model):
    _inherit = "res.users"

    abc = fields.Char()
    xyz=  fields.Char()
    
    #Relations Fields
    property_ids = fields.One2many(
        "estate.property", "salesperson_id", string="Properties")
    
