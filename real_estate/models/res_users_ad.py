from odoo import api, models, fields

class InheritedRes(models.Model):
    _inherit="res.users"

    property_ids=fields.One2many('real.estate.properties','user_id',string="Property")
    # domain=['|', ('state', '=', 'new'), ('state', '=', 'offer_received')]