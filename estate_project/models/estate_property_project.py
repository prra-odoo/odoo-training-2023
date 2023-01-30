# -*- coding: utf-8 -*-

from odoo import models, fields
from dateutil.relativedelta import relativedelta

class EstatePropertyAccount(models.Model):
    _inherit = "estate.property"
        
    def action_sold_btn(self):

        #Create project task, When property was sold.
        
        estate_task = self.env['project.task'].sudo().create(
            {
                'name': 'Clean '+ self.name,
                'project_id': 4,
                'stage_id': 1,
                'planned_date_begin': fields.Datetime.today(),
                'planned_date_end': fields.Datetime.today() + relativedelta(hours=+8),
            }            
        )
        return super().action_sold_btn()
