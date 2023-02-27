from odoo  import models, fields
class User(models.Model):
    _inherit="res.users"


    num=fields.Float()
    property_ids=fields.One2many('estate.property','user_id',domain="[('state', 'in',['new','offer received'])]")   