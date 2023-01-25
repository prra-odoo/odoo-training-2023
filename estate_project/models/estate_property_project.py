# -*- coding: utf-8 -*-

from odoo import models

class estate_project(models.Model):

    _inherit=['real.estate.properties']

    def action_sold(self):
        # a=self.env['project.project'].create({
        #          'name' : 'Task'
        #      })
        for record in self:
            self.env['project.task'].create({
                    'name' : 'Cleaning',
                    'project_id' : 15,
                    'partner_id' : record.buyer.id,
                })

        return super().action_sold()
            