# -*- coding: utf-8 -*-
from odoo import http

class Academy(http.Controller):

    # @http.route('/academy/<model("estate.property"):teacher>/', auth='public', website=True)
    # def teacher(self, teacher):
    #     return http.request.render('Estate.index', {
    #     'person': teacher
    # })
      
    #  @http.route('/academy/<name>/', auth='public', website=True)
    #  def teacher(self, name):
    #     return '<h1>{}</h1>'.format(name)
     
    #  @http.route('/property/', auth='public', website=True)
    #  def index(self, **kw):
    #      property = http.request.env['estate.property']
    #      return http.request.render('Estate.index', {
    #          'property': property.search([]),
    #      })
     @http.route('/property/<model("estate.property"):property>', auth='public', website=True)
     def index1(self, property):
        return http.request.render('Estate.property_details_view',{
            'plot': property
            })
     

     @http.route(['/property/','/property/page/<int:page>'], auth='public', website=True)
     def index(self,page=0,search='', **kw):
        domain=[]
        if search:
            domain.append(('name','ilike',search))
        properties = http.request.env['estate.property'].search(domain)
        total_properties = properties.sudo().search_count([])
        pager = http.request.website.pager(
            url='/property/',
            total = total_properties,
            page=page,
            step=2,
            url_args=None,
        )
        package = http.request.env['estate.property'].search(domain,limit=2,offset=pager['offset'],order='id desc')
        return http.request.render('Estate.index',{
            'property' : package,
            'pager' : pager,
        })

