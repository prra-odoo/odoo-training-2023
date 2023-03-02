from odoo import fields,models,Command

class EstateProperty(models.Model):
    _inherit = "estate.property"

    def sold_action_button(self):
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
        return super(EstateProperty,self).sold_action_button()