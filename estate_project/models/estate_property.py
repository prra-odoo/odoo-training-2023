# -*- coding: utf-8 -*-
from odoo import models,fields,api
from odoo.exceptions import UserError,ValidationError


class estate_property(models.Model):
    _name = 'estate.property'
    _inherit = 'estate.property'
    _description = "Real Estate Module"

    def action_sold(self):
        # print("hellooooooo")
        # breakpoint()
        # project_id = 0
        p_exists = self.env['project.project'].search([('name','=','new project')])

        if p_exists:
            project_id = p_exists.id
        else :
            stage = self.env['project.project'].create(
                {
                    'name':'new project',
                })
            project_id = stage.id
                
        self.env['project.task'].create(
            {
                'name':self.name,
                'project_id':project_id,
            }
        )
        return super().action_sold()





        # stage = self.env['project.project'].create(
        #     {
        #         'name':'Estate Property',
        #     }
        # )
        # self.env['project.task'].create(
        #     {
        #         'name':self.name,
        #         'project_id':5,
        #         # 'date':fields.Date.context_today(self),
        #     }
        # )
        # return super().action_sold()