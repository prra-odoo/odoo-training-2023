# -*- coding: utf-8 -*-
from odoo import http

class Estate_web(http.Controller):
    
    @http.route('/myproperty',auth='public',website=True)
    def mainindex(self, **kw):
        properties = http.request.env['estate.property.model']
        return http.request.render('real_estate.mainp',{
            'properties': properties.search([])
        })

    @http.route('/myproperty/properties',auth='public',website=True)
    def index(self, **kw):
        properties = http.request.env['estate.property.model']
        return http.request.render('real_estate.desp',{
            'properties': properties.search([])
        })


    @http.route('/myproperty/<model("estate.property.model"):id>/',auth='public',website=True)
    def propert(self,id):
        return http.request.render('real_estate.desp',{
            'property': id
        })

    @http.route('/myproperty/1',auth='public',website=True)
    def paging(self, **kw):
        return http.request.render('real_estate.pagin')