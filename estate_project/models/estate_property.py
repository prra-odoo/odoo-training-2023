# -*- coding: utf-8 -*-

from odoo import models, fields, Command

class EstateProject(models.Model):
    _inherit = "estate.property"

    def action_sold(self):
        self.env["project.task"].create(
            {
                'partner_id': self.buyers_id.id,
                'name': self.name,
                'project_id' : 3,
            }
        )
        return super(EstateProject,self).action_sold()
        