# -*- coding: utf-8 -*-

from odoo import models,Command

class estateProject(models.Model):
    _inherit = "estate.property"

    def sold_button(self):
       for record in self:
            
            records = self.env['project.project'].create(
                {
                    "name": record.name,
                    
                })
            self.env['project.task'].create(
                {
                    "name": record.name,
                    "project_id": records.id
                })
            return super().sold_button()
