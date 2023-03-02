from odoo import models,fields,Command

class EstateProperty(models.Model):
    _inherit = "estate.property"

    def action_sold(self):
    
        project_obj = self.env['project.project'].create({
            'name': 'Estate Project',
            'partner_id': self.buyer_id.id,
            'type_ids': [
                Command.create({'name': 'Renovation', 'sequence': 1, 'fold': False}),
                Command.create({'name': 'Paint', 'sequence': 2, 'fold': False}),
                Command.create({'name': 'Payment and Paper Work', 'sequence': 3, 'fold': False})
            ]
        })
        task_obj_1 = self.env['project.task'].create({
            'name': 'Task 1',
            'project_id': project_obj.id
        })
        task_obj_2 = self.env['project.task'].create({
            'name': 'Task 2',
            'project_id': project_obj.id
        })
        
        return super().action_sold()