# -*- coding: utf-8 -*-
from odoo import models,Command

class EstateProperty(models.Model):
    _inherit = "estate.property"

    def action_sold(self):
        vals = {
            'partner_id':self.buyer_id.id,
            'name':self.name,
            'tasks':[Command.create({"name":"Maintainance task"})]
        }
        self.env["project.project"].create(vals)
        return super(EstateProperty,self).action_sold()
    

    # project = self.env['project.project'].create({
    #         'name': self.name,
    #     })

    #     task = self.env['project.task'].create({
    #         'name' : "Maintance",
    #         'project_id' : project.id
    #     })