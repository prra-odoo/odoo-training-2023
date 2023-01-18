from odoo import fields, models

class inheritance_demo(models.Model):
    _inherit = 'estate.property.type'
    _name = 'inheritance.demo'
    
    demo = fields.Char('demo inheritance')
    abc = fields.Char('abc')