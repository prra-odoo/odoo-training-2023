# -*- coding: utf-8 -*-
from datetime import datetime
from odoo import api, fields, models, Command, _


class estateProperty(models.Model):
    _inherit = "estate.property"
    _description = "Inherit Estate Model"

    def action_sold(self):
        if not self.env['project.project'].search([('name', '=', 'Estate Property')]).id:
            self.env['project.project'].create({
                'name': 'Estate Property',
            })

        for rec in self:
            task_1 = self.env['project.task'].create({
                'name': f'Maintainance for {rec.name}',
                'project_id': self.env['project.project'].search([('name', '=', 'Estate Property')]).id,
                'milestone_id': 2,
                'planned_date_begin': datetime.today(),
                'planned_date_end': datetime(2023, 2, 1, 17, 0),
            })

        return super().action_sold()
