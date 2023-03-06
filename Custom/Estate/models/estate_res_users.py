from odoo import fields,models

            #CLASSIC INHERITANCE
class ResUsers(models.Model):
    _inherit="res.users"

    property_ids = fields.One2many('estate.property','salesperson_id',domain=[('state','in',['new','offer received'])])
    testing = fields.Char()

