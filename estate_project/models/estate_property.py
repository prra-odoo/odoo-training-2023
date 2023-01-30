from odoo import models,fields,Command

class Inherited_Estate_For_Project(models.Model):
    _inherit="estate.property.model"

    name=fields.Char(required=True)

    def perform_sold(self):
        print(" reached ".center(100, '='))
        self.env['project.project'].check_access_rights('read')
        self.env['project.project'].check_access_rights('write')
        # self.env['project.project'].check_access_rule('write')
        print(self.env.user.has_group)
        self.env['project.project'].sudo().create({
            'name': 'Cleaning Property',
            'task_ids': [
                Command.create({
                    'name': 'Cleaning Wrok',
                })
            ]
        })
        return super().perform_sold()


