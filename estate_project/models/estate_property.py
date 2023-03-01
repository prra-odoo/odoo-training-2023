from odoo import models

class EstateProperty(models.Model):
    _inherit="estate.property"

    def action_sold(self):
        self.env['project.project'].create({
            'name':self.name,
            })
        return super[EstateProperty,self].action_sold()