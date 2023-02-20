# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request


class Estate(http.Controller):

#<--------------render through the statically from the python code--------------->
# 	@http.route('/estate/properties/',auth='public')
# 	def index(self, **kw):
# 		return http.request.render('estate.index',{
# 			'users':['Althaf','mitchell Admin','mark demo']
# 			})

#<------------------render through the database------------------------>
	# @http.route('/estate/properties/',auth='public',website=True)
	# def index(self,**kw):
	# 	Properties=http.request.env['estate.property']
	# 	return http.request.render('estate.index',{
	# 		'properties':Properties.search([('state','in',['new','offer_recieved','offer_accepted'])])
	# 		})
#<-------------------routing a bit of url and print it out as variable--------->
	# @http.route('/estate/<name>/', auth='public', website=True)
	# def property(self, name):
	# 	return '<h1>{}</h1>'.format(name)

#<------------routing a bit a url and validating and coonversion------------>
	# @http.route('/estate/<int:id>/',auth='public',website=True)
	# def property(self,id):
	# 	return '<h1>{} ({})</h1>'.format(id,type(id).__name__)

#<-----------model converter----------------->
	@http.route('/estate/<model("estate.property"):property>/',auth='public',website=True)
	def property(self,property):
		return http.request.render('estate.property_details',{
			'details':property
			})
	@http.route(['/estate/properties','/estate/properties/page/<int:page>'],type="http",auth='public',website=True)
	def index(self,page=1, **kw):
		domain=[('state','in',['new','offer_recieved','offer_recieved','offer_accepted'])]
		Properties=http.request.env['estate.property'].search(domain)
		total=Properties.search_count([])
		pager=http.request.website.pager(
			url='/estate/properties',
			total=total,
			page=page,
			step=9
		)
		pagerProperties = Properties.search(domain,offset=(page - 1)* 9, limit=8)
		return http.request.render('estate.index',{
			'properties':pagerProperties,
			'pager':pager
			})