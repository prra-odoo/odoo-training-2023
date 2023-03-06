from odoo import models , fields , Command

class EstateProperty(models.Model):
    _inherit="estate.property"

    def action_set_sold(self):
        self.env['project.project'].create(
            {
            "name":self.name,
            'partner_id':self.buyer.id,
            'task_ids':[
            Command.create(
            {
            'name':'maintenance',
            }
            )
            ]
            }
        )
        return super().action_set_sold()