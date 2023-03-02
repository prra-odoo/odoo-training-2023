from odoo import api,fields, models, Command

class EstateProperty(models.Model):
    # _description = "estate property"
    _inherit="estate.property"

    def action_sold(self):

        print("hello")
        self.env['project.project'].create({
            'name':self.name,
            'partner_id':self.buyer.id,
            'task_ids':[
                Command.create({
                'name':'maintenance',
                })
            ]
        })
        return super().action_sold()