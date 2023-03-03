from odoo import models,fields,Command


class EstateProperty(models.Model):
    _inherit = "estate.property"

    def action_sold(self):
      for record in self:
        project= self.env["project.project"].create(
        {
            "name":record.name,
            "task_ids": [
                (0,0, 
                 {   'name':"Maintenance"
                 })
                    ]

            
            
        })
        # self.env["project.task"].create({
        #    "name":"Maintenance",
        #    "project_id":project.id

        # })
    
        return super().action_sold()


