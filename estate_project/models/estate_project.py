# -*- coding: utf-8 -*-

from odoo import Command
from odoo import models
from datetime import date


class EstatePropertyProject(models.Model):
    _inherit = "real.estate"
    
    def sold_button(self):
        for rec in self:
            if not self.env['project.project'].search([('name', '=', 'Project')]).id:
                project= self.env['project.project'].create({
                    'name' : 'Project',
                })
            
            task = self.env['project.task'].create({
                'name' : rec.name,
                'project_id': self.env['project.project'].search([('name', '=', 'Project')]).id,
            })
        return super().sold_button()

   