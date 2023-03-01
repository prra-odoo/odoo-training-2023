# -*- coding: utf-8 -*-
from odoo import models, Command

class EstateProperty(models.Model):
    _inherit = 'estate.property'

    def action_sold(self):
        # breakpoint()
        # print('in acount estate')

        self.env['project.project'].create(
        {
        # 'partner_id':self.buyer_id.id,
        'name': self.name,
        'task_ids': [
                Command.create({
                    'name': 'Maintenence',
                    'partner_id':self.buyer_id.id,
                })]
                })
        return super(EstateProperty,self).action_sold()