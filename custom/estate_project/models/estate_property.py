from odoo import models,fields
class EstateProperty(models.Model):
    _inherit = "estate.property"

    def sold_action(self):
        self.env['project.project'].create(
            {
            'name':self.name
            }
        )
        return super(EstateProperty,self).sold_action() 