from odoo import models,fields,Command


class EstateProperty(models.Model):
    _inherit = "estate.property"

    def action_sold(self):
        project= self.env["project.project"].create(
        {
            "name":self.name,
            
            
        })
        self.env["project.task"].create({
           "name":"Maintenance",
           "project_id":project.id

        })
    
        return super().action_sold()


