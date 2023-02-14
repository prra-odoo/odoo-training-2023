from odoo import models,fields

class AcomPropertyRoomModel(models.Model):
    _name = "acom.prop.room"
    _description = "this is the Property Type Model"

    name = fields.Char(required=True)