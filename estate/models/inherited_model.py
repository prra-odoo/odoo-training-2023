# -*- coding: utf-8 -*-


from odoo import models, fields, api

class InheritedClass(models.Model):
    # _name  = "inherited.model"
    _inherit = "res.users"
    # _description = "new"

    # groups_id = fields.Many2many('res.groups', 'inherited_users_rel', 'uid', 'gid', string='Groups')
    # company_ids = fields.Many2many('res.company', 'inherited_users_rel', 'user_id', 'cid',string='Companies')
    property_ids = fields.One2many('estate.property','salesperson_id',string="Property Id")
    demo = fields.Char('Demo')
    check = fields.Boolean('Check')

class DelegationClass(models.Model):
    _name = "estate.property.customer"
    _inherits = {
        'estate.property' : 'Property_id'
    }

    property_id = fields.Many2one('estate.property',string="Estate Property")   
    demo = fields.Char()
    
