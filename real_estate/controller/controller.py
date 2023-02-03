
# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class Academy(http.Controller):

    @http.route(['/estate/properties/','/estate/properties/page/<int:page>'],website=True, auth='public')
    def index(self, page=0, search=''):
        # return "Hello, world"
        domain = []
         
        if search:
            domain=[('name','ilike',search)]

        total_property = http.request.env['estate.property'].search(domain)
        total_count  = len(total_property)
        per_page = 4
        pager = request.website.pager(url='/estate/properties',total=total_count, page=page, step=per_page, scope=3, url_args=None)

        properties = request.env['estate.property'].search(domain,limit=per_page, offset=pager['offset'],order='id asc')
        return http.request.render('real_estate.property_page',{
                'properties':properties,
                'pager':pager,
        })
        # return http.request.render('real_estate.property_page', {
        #      'properties': properties.search([])
        # })



        # properties = http.request.env['estate.property']
        
        # return http.request.render('real_estate.property_page', {
        #      'properties': properties.search([])
        # })
        # return http.request.render('real_estate.website_page_test',{})

    # # New route
    # @http.route('/estate/<name>/', auth='public', website=True)
    # def teacher(self, name):
    #     return '<h1>{}</h1>'.format(name)

    
    @http.route('/real_estate/<model("estate.property"):property>/', auth='public', website=True)
    def teacher(self, property):
        return http.request.render('real_estate.description', {
        'property': property
        })