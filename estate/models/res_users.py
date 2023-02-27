from odoo import models , fields
 
class Users(models.Model):
    _inherit="res.users"

    property_id=fields.One2many("estate.property","salesperson")
    numbs= fields.Float()