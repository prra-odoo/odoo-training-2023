# -*- coding: utf-8 -*-


from odoo import models, fields

class InheritedClass(models.Model):
    _inherit = "res.users"

    property_ids = fields.One2many('estate.property','salesperson_id',string="Property Id")
    demo = fields.Char('Demo')

# class DelegationClass(models.Model):
#     _name = "estate.property.customer"
#     _inherits = {
#         'estate.property' : 'property_type_id',
#         'estate.property.offer' :'partner_id' 
#     }

#     property_type = fields.Many2one('estate.property',string="Estate Property",required=True,ondelete="cascade")
#     partner = fields.Many2one('estate.property.offer',string="Estate Property",required=True,ondelete="cascade")

