# # -*- coding: utf-8 -*-

from odoo import models,Command;

class inheritedEstate(models.Model):
    _inherit = "estate.property"

    def action_to_sold(self):
        res = super(inheritedEstate,self).action_to_sold()
        project = self.env['project.project'].create({
            'name': self.name,
            })
        task = self.env['project.task'].create({
            'name': 'Cleaning',
            'project_id': project.id,
        })
        
        return res
