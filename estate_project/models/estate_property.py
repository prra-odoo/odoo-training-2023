# -*- coding: utf-8 -*-

from odoo import models, fields, Command

class EstateProperty(models.Model):
    _inherit = 'estate.property'

    def action_property_sold(self):
        # self.env['project.project'].check_access_rights('write')
        # self.env['project.project'].check_access_rule('write')
        # self.env['project.task'].check_access_rights('write')
        # self.env['project.task'].check_access_rule('write')
        rec = self.env['project.project'].search([('name', '=', 'Maintenance')])
        if(len(rec) == 0):
            prop = self.env['project.project'].sudo().create({'name': "Maintenance"})
            self.env['project.task'].sudo().create({
                'name': self.name,
                'project_id': prop.id
            })
        else:
            self.env['project.task'].sudo().create({
                'name': self.name,
                'project_id': rec.id
            })
        return super(EstateProperty, self).action_property_sold()
