from odoo import models,fields,Command

class EstateProperty(models.Model):
    _inherit = ['estate.property']

    def action_do_sold(self):
        self.env['project.project'].create({
            'name': self.name,
            'task_ids' : [
                Command.create({
                    'name' : 'Maniitance',
                }),
            ]
        })
        return super(EstateProperty,self).action_do_sold()
    