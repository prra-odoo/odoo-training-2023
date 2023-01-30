# -*- coding: utf-8 -*-

from odoo import models, fields, api, SUPERUSER_ID

class EstateProperty(models.Model):
    _inherit = "estate.property"

    def property_sold(self):
            project = self.env['project.project'].search([('name','=','Maintenance')])

            if project:
                project_id = project.id
            else :
                newProject = self.env['project.project'].sudo().create(
                    {
                        'name':'Maintenance',
                    })
                project_id = newProject.id

            self.env['project.task'].create(
                {
                    'name':self.name,
                    'project_id':project_id,
                }
            )
            return super().property_sold()
    
