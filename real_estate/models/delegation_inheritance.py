from odoo import fields, models

class delegation_inheritance(models.Model):
    _name = 'delegation.inheritance'
    _inherits = {'estate.property.type':'type_id'}
    
    type_id = fields.Many2one('estate.property.type','delegation')
    demo = fields.Char('demo inheritance')
    xyz = fields.Char('abc')