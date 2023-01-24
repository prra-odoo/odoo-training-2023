from odoo import models,Command

class EstateProject(models.Model):
    _inherit="real.estate.property"

    def action_state_sold(self):
        for record in self:
            pro=self.env['project.project'].search([('name','ilike','Cleaning')])
            if not pro:
                pro=self.env['project.project'].create({
                    'name':'Cleaning'
                })
            self.env['project.task'].create({
                'project_id':pro.id,
                'name':'Maintenance:'+record.name
            })
        return super().action_state_sold()