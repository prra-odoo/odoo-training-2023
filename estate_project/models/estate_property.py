from odoo import models,Command

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property Model"
    _inherit = 'estate.property'

    def action_sold(self):
        values = {'name':self.name,'partner_id':self.buyer_id.id,'task_ids':[Command.create({"name":"Maintainance"})]}
        self.env['project.project'].create(values)    
        return super().action_sold()