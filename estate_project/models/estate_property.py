from odoo import fields,models,Command

class EstateProperty(models.Model):
    _inherit = "estate.property"


    def action_sold(self):

        project = self.env['project.project'].create({
            'name':self.name
        })

        task1 = self.env['project.task'].create({
            'name': 'Task-1',
            'project_id': project.id
        })  

        maintenance = self.env['project.task'].create({
            'name': 'Maintenance',
            'project_id': project.id
        })    

        return super().action_sold()