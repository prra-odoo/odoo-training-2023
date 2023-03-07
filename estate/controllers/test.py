# -*- conding: utf-8 -*-
from odoo import http

class TestController(http.Controller):
	@http.route('/test', auth='public', website=True)
	def index(self, **kw):
		property = http.request.env['estate.property']
		return http.request.render('estate.index',{
			'property':property.search([])
			})

	@http.route('/properties', auth='public', website=True)
	def prop(self, **kw):
		property = http.request.env['estate.property']
		return http.request.render('estate.properties',{
			'property':property.search([])
			})

