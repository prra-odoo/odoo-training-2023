# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request

class EstateController(http.Controller):
    # ROUTE 1
    # @http.route('/estate/<name>/', auth="public", website=True)
    
    # def index(self, name):
    #     return '<h1>Good Afternoon {}</h1>'.format(name)
    
    # ROUTE 2
    # @http.route('/estate/<int:id>/', auth="public", website=True)
    
    # def index(self, id):
    #     return '<h1>Good Afternoon {}</h1>'.format(id)
    
    # ROUTE 3
    @http.route('/estate/estate/', type="http", auth="public", website=True)
    
    def index(self, **kw):
        estate_property = request.env['estate.property'].sudo().search([])
        data = {
            'records': estate_property
        }
        return request.render("real_estate.demo_controller_template", data)
    
    # ROUTE 4
    @http.route('/estate/<model("estate.property"):property>/', auth='public', website=True)
    
    def estate(self, property):
        return http.request.render('real_estate.single_property_template', {'record': property})