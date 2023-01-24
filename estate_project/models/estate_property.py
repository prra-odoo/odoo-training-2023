# -- coding: utf-8 --
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields,models
from datetime import datetime

class RealEstateProperty(models.Model):
    _inherit =  "real.estate.property"
    
    def action_sold_porperty(self):
        print(self)
        res = super().action_sold_porperty()
        project = self.env['project.project'].search([('name', '=', 'Test Task')])
        print(project,"fgfc cvgvvgh")
        self.env["project.task"].create(
            {
                'name': 'Clean '+ self.name,
                'project_id': project.id,
                # 'user_ids': self.user_hruser,
                'planned_date_begin': datetime.today(),
                'planned_date_end': datetime.today(),
            }
        )
        print(res)
        return res