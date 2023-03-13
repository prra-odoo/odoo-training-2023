from odoo import models,fields,api,Command

class EstateRealProperty(models.Model):
    _name="estate.property.project"
    _inherit="estate.real.property"
    
    def action_sold(self):
        
        project=self.env['project.project'].create({
            'name': self.name,
            'partner_id': self.buyer_id.id,
        })
        self.env['project.task'].create({
            'name': 'Maintainence Task One',
            'kanban_state': 'normal',
            'project_id':project.id,
            'partner_id': self.buyer_id.id,})
        
        return super().action_sold()
 