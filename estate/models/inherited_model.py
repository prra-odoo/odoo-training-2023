# -*- coding: utf-8 -*-

from odoo import models, fields

# ________________Classic Inheritance__________________

class InheritedModel(models.Model):
    _inherit = "res.users"

    property_ids = fields.One2many('estate.property', 'sales_id', string='Properties', domain=[('state', 'in', ['new', 'offer_received'])])
    sold_property_ids = fields.One2many('estate.property', 'sales_id', domain=[('state', '=', 'sold')])

# _________________Prototype Inheritance________________

# class InheritedModel(models.Model):
#     _name = "new"
#     _inherit = "estate.property"

#     demo = fields.char()

# _________________Delegation Inheritance_________________

# class InheritedModel(models.Model):
#     _name = "new"
#     _inherits = {'res.partner': 'partner_id'}

#     partner_id = fields.Many2one('res.partner', required=True)
#     website_partner = fields.Char(related='partner_id.website', required=True, inherited=True, store=True)
