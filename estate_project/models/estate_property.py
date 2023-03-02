# -*- coding: utf-8 -*-
from odoo import models,Command

class EstateProperty(models.Model):
    _inherit = "estate.property"

    def action_sold(self):
        vals = {
            'partner_id':self.buyer_id.id,
            'name':self.name,
            'task_ids':[Command.create({"name":"Maintainance"})]
        }
        self.env["project.project"].create(vals)
        return super(EstateProperty,self).action_sold()
