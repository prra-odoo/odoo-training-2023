from odoo import models


class EstatePropertypProject(models.Model):
    _inherit = "estate.property"

    def sold_action(self):
        for record in self:
            if not self.env['project.project'].search([('name', '=', 'Property Task')]).id:
                project = self.env['project.project'].create({
                'name': 'Property Task',
                })
            
            
            task_names = 'Property Maintenance.' + self.name
            task= self.env['project.task'].sudo().create({
                    'name': task_names,
                    'description': 'Task for maintenance of property ' + self.name,
                    'project_id':  self.env['project.project'].search([('name', '=', 'Property Task')]).id,
            })
        return super().sold_action()