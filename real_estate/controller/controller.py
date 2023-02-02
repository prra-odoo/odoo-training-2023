
# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class Academy(http.Controller):

    @http.route('/estate/properties/',website=True, auth='public')
    def index(self, **kw):
        # return "Hello, world"
        properties = http.request.env['estate.property']
        
        return http.request.render('real_estate.property_page', {
             'properties': properties.search([])
        })
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