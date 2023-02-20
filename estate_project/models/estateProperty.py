# -- coding: utf-8 --
from odoo import fields,models,api,Command

from dateutil.relativedelta import relativedelta

class estateProperty(models.Model):
    _name = "estate.property"
    _inherit= "estate.property"

   
    def sell_property(self):
        
        print("Project Created")

        if not self.env['project.project'].search([('name','=',"Cleaning")]):
            self.env['project.project'].create({
                'name': "Cleaning",
            })

        # estate_project = self.env['project.project'].create({
        #     'name': self.name,
        # })
        project=self.env['project.project'].search([('name','=',"Cleaning")])

        self.env['project.task'].create({
            'name': self.name,
            'project_id': project.id,
            'partner_id': self.buyer_id.id,
            'date_deadline': fields.datetime.now() + relativedelta(days=1)
        })

        
        return super().sell_property()
