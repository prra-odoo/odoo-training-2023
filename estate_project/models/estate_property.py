from odoo import models,fields,Command

class EstateProperty(models.Model):
    _inherit = "estate.property"

    def action_set_state_sold(self):
        name = self.name
        task = [
            Command.create({
                'name': 'maintenance'
            }),
        ]
        self.env['project.project'].create({
            'name':name,
            'tasks': task
        })
        return super(EstateProperty,self).action_set_state_sold()