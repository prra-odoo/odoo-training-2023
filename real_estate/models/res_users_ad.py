from odoo import api, models, fields

class InheritedRes(models.Model):
    _inherit="res.users"

    property_id=fields.One2many('real.estate.properties','user_id',domain="[('state', 'in', ('new','offer received))]")