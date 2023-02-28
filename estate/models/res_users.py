from odoo import models , fields

class ResUsers(models.Model):
    _inherit="res.users" 
    # _here name is not necessary bcoz we manipulate in the same model

    property_ids=fields.One2many("estate.property","user_id" , string="Properties" , domain="[('state' , 'in',('new','offer_received'))]")
    numbs= fields.Float()