# -*- coding: utf-8 -*-
from odoo import http

class real_estate(http.Controller):
    @http.route('/estate/estate/',auth='public' ,website=True)
    def index(self,**kw):
        Property =  http.request.env['estate.property.type']
        Tags =  http.request.env['estate.property.tag']
        return http.request.render('estate.index',{
            'properties' : Property.search([]),
            'tags' : Tags.search([])
        })
    
    @http.route('/estate/<model("estate.property.tag"):properties>/',auth='public',website=True)
    def property(self,properties):
        return http.request.render('estate.template_controller',{
            'prop' : properties
        })  