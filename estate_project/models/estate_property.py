# -*- coding: utf-8 -*-

from odoo import models

class estateProperties(models.Model):
    _inherit = "estate.property"
    
    def action_sold(self):
        
        self.env['project.task'].create({
            'name' : self.name,
            'project_id' : 4,
            'partner_id' :  self.buyers_id.id
        })
        
        return super(estateProperties,self).action_sold()