from odoo import  models

class EstateTask(models.Model):
    _inherit ="real.estate.properties"

    def action_sold(self):
        for record in self:
            self.env['project.task'].create(
                {   
                    "name":'Cleaning',
                    "project_id":4,
                    "partner_id":record.buyer_id.id
                }
            )

        return super().action_sold()