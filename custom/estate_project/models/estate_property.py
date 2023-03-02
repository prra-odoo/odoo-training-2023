from odoo import models,Command

class EstateProperty(models.Model):
    _inherit = 'estate.property'

    def action_sold(self):
       self.env['project.project'].create({
           'name': self.name,
           'partner_id': self.buyer_id.id,
           'type_ids': [
           Command.create({
                'name': 'New',
                'sequence': 1
           }),
           Command.create({
                'name': 'In progress',
                'sequence': 2
           }),
           Command.create({
                'name': 'Done',
                'sequence': 3
           })],
           'task_ids': [
           Command.create({
                'name': 'maintenance',
           })]
       })
       return super().action_sold()