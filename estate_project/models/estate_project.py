# -*- coding: utf-8 -*-
from odoo import models


class projectEstateModel(models.Model):
    _inherit = 'estate.property'

    

    def sold_product(self):
        print(self.name)
        project = self.env['project.task']
        self.env['project.task'].sudo().create(
            {
                'name': self.name,
                'project_id': 4,
                'partner_id':self.buyer_id.id

            }
        )
        return super().sold_product()


    # def sold_product(self):
    #     project = self.env['project.project'].create({
    #         'name': self.name,
    #         })
    #     self.env['project.task'].create({
    #         'name': 'Cleaning',
    #         'project_id': project.id,
    #     })
    #     return super().sold_product()
        
