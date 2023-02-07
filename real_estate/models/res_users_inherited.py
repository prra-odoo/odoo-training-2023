# -*- coding: utf-8 -*-

from odoo import models, fields

#---------------- Class Inheritance ----------------#
class ResUsersInherited(models.Model):
    _name = "res.users"
    _inherit = "res.users"
    
    property_ids = fields.One2many("estate.property", "salesperson_id", string="Property IDs")

#---------------- Prototype Inheritance ----------------#  
# class MyEstateProperty(models.Model):
#     _name = "my.estate.property"
#     _inherit = "estate.property"
#     _description = "Testing"
    
#     test = fields.Char(string="Testing")

#---------------- Delegation Inheritance ----------------# 
# class MyEstateProperty(models.Model):
#     _name = "my.estate.property"
#     _inherits = {'estate.property': 'property_name_id'}
#     _description = "Testing"
    
#     property_name_id = fields.Many2one('estate.property')
#     test1 = fields.Char(string="Testing")
    
#     print(property_name_id)
