from odoo import models,fields

class res_user(models.Model):
    
    _inherit='res.users'

    property_ids=fields.One2many('estate.property','sales_id')
    demo=fields.Integer()
    