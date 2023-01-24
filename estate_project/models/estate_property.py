from odoo import models,fields,Command

class Inherited_Estate_For_Project(models.Model):
    _inherit="estate.property.model"

    name=fields.Char(required=True)

    def perform_sold(self):
        self.env['project.project'].create({
            'name': 'Cleaning Property',
            'task_ids': [
                Command.create({
                    'name': 'Cleaning Wrok',
                })
            ]
        })
        return super().perform_sold()


