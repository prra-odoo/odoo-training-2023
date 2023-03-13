from odoo import models,fields,Command
class EstateProperty(models.Model):
    _inherit = "estate.property"

    def sold_action(self):
        project=self.env['project.project'].create(
            {
            'name':self.name,
            'type_ids':[
             Command.create({
            'name':'New'
             })

            ]
            }
        )
        # task=
        self.env['project.task'].create(
            {
            'project_id':project.id,
            'name':'maintenance'

            }
        )

        return super(EstateProperty,self).sold_action() 