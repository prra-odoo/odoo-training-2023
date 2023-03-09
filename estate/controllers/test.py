# -*- conding: utf-8 -*-
from odoo import http

class TestController(http.Controller):
	@http.route(['/properties','/properties/page/<int:page>'], auth='public', website=True)
	def prop(self,page=1, **kw):
		domain=[('state','not in',['sold','cancelled'])]
		Properties = http.request.env['estate.property'].search(domain,offset=(page-1)*3, limit=3)
		total = Properties.search_count([])
		pager = http.request.website.pager(
			url='/properties',
			total=total,
			page=page,
			step=2,
	)
		return http.request.render('estate.properties',{
			'properties' : Properties,
			'pager':pager,
			})

	@http.route('/test/<name>/', auth='public', website=True)
	def teacher(self, name):
		return '<h1>{}</h1>'.format(name)

	@http.route('/properties/<model("estate.property"):property>', auth='public', website=True)
	def index(self, property):
		return http.request.render('estate.property_details_view',{
			'plot': property
			})