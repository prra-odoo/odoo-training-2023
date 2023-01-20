from odoo import models,fields

class InheritanceResUser(models.Model):
    _inherit = "res.users"
    
    property_ids = fields.One2many("real.estate.property" , "salesperson_id" , string="user inherit" , domain = "[('state', 'in', ['new' , 'offer_accepted'])]")
    # nammmmmmmmme = fields.Char()