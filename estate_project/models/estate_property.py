from odoo import models

class EstateProperty(models.Model):
    _inherit="estate.property"

    def action_sold(self):
        project=self.env['project.project'].create({
            'name':self.name,
            })
        
        task=self.env['project.task'].create({
            'name':("Maintenance"),
            'project_id': project.id
        })
        return super().action_sold()