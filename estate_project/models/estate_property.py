# -*- coding: utf-8 -*-

# from odoo import models,fields,Command

# class estateProject(models.Model):
# 	_inherit='estate.property'

# 	def sold_button(self):
# 		project= self.env['project.project'].create({
# 			'name':self.name,
# 			})
# 		self.env['project.task'].create({
# 			'name':self.name,
# 			'project_id':project.id,
# 			'partner_id':self.buyer_id.id
# 			})
# 		return super().sold_button()