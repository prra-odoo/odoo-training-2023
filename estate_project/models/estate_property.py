# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields,models

class EstateProperty(models.Model):
    _inherit="estate.properties"

    def action_sold(self):
        # project= self.env["project.project"].search(["name",'=','Cleaning property']) 
        for record in self:
            self.env["project.task"].sudo().create({
                'name': "clean "+ record.name,
                'project_id' : 4,
                "partner_id":record.buyer_id.id
            }
            )
        return super().action_sold()