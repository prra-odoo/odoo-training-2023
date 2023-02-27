from odoo import models,fields,api

class InheritedModel(models.Model):
    _inherit = "res.users"

    property_ids=fields.One2many('estate.property','salesperson_id')
    # price =fields.Char()
    # date=fields.Date()
    # postcode=fields.Integer()








    