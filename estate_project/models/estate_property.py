from odoo import models,fields

class EstateProperty(models.Model):
    _inherit = "estate.property"

    def action_sold(self):
        project = self.env['project.project'].create({
            'name': 'Estate Project',
            'allow_timesheets': True,
            'partner_id': self.buyer_id.id,
        })
        return super().action_sold()