from odoo import models , fields

class EstateProperty(models.Model):
    _inherit="estate.property"

    def action_set_sold(self):
        self.env['project.project'].create(
            {
            "name":self.name
            }
        )
        # newtask =self.env['project.task'].create(
        #     {
        #     "name":"newtask", 
        #     "project_id":project.id
        #     }
        # )
        return super().action_set_sold()
    


