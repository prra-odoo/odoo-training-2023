# -*- coding: utf-8 -*-

from odoo import fields, models

class inheritedModel(models.Model):
    # _name = "inherited.model"
    _inherit = 'res.users'

    property_ids = fields.One2many("estate.property", "salesperson_id", string = "Properties")
    name = fields.Char()
    demo=fields.Char()

# class inheritedModel1(models.Model):
#     _name = "inherited.model1"

#     demo1 = fields.Char()

# class inheritedModel2(models.Model):
#     _name = "inherited.model2"
    
#     _inherits={'inherited.model': 'demo_id',
#                 'inherited.model1': 'demo1_id'}

#     name = fields.Char()

#     demo_id = fields.Many2one("inherited.model")
#     demo1_id = fields.Many2one("inherited.model1")
