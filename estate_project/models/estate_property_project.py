# -*- coding: utf-8 -*-
from odoo import models,fields
from dateutil.relativedelta import relativedelta

class EstatePropertyProject(models.Model):
    _inherit = "estate.property"

    def action_sold_btn(self):
        print("======")
        print("Project Created")
        estate_project = self.env['project.project'].create({
            'name': self.name,   
        })
        estate_task = self.env['project.task'].create({
            'name': "Clean",
            'project_id': estate_project.id,
            'partner_id': self.buyer_id.id,
            'date_deadline': fields.datetime.now() + relativedelta(days=1)
        })

        return super().action_sold_btn()