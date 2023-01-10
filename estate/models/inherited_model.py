# -*- coding: utf-8 -*-


from odoo import models, fields

class InheritedClass(models.Model):
    _inherit = "res.users"

    property_ids = fields.One2many('estate.property','salesperson_id',string="Property Id")
    demo = fields.Char('Demo')