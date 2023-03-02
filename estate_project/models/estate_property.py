# -- coding: utf-8 --
from odoo import models,Command

class EstateProperty(models.Model):
    _inherit = "estate.property"

    def action_sold(self):
        self.env['project.project'].create(
            {
                    'partner_id':self.buyer_id.id,
                    'name':self.name,
                    'tasks': [
                            Command.create({
                                "name":"Maintainance task"
                            })
                        ]
            }
        )
        return super(EstateProperty,self).action_sold()