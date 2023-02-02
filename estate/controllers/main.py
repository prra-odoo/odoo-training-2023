# -*- coding: utf-8 -*-
from odoo import http

class real_estate(http.Controller):
    @http.route('/estate/estate/',auth='public' ,website=True)
    def index(self,**kw):
        Property =  http.request.env['estate.property']
        return http.request.render('estate.index',{
            'properties' : Property.search([]),
        })
        
        
    # @http.route('/estate/<name>/', auth='public', website=True)
    # def property(self, name):
    #     return '<h1>{}</h1>'.format(name)
    
    # @http.route('/estate/<int:id>/', auth='public', website=True)
    # def property(self, id):
    #     return '<h1>{} ({})</h1>'.format(id, type(id).__name__)
    
    @http.route('/estate/<model("estate.property"):properties>/',auth='public',website=True)
    def property(self,properties):
        return http.request.render('estate.template_controller',{
            'prop' : properties
        })  