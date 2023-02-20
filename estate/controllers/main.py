# -*- coding: utf-8 -*-
from odoo import http


class EstatePropertyController(http.Controller):
    @http.route('/estate', type='http', auth="public",website=True)
    def hello(self,**kw):
        property = http.request.env['estate.property']
        return http.request.render('estate.index', {
             'properties': property.search([])
         })


    @http.route('/estate/<model("estate.property"):prop>/', type='http', auth="public",website=True)
    def index(self,prop):
        return http.request.render('estate.index',{
            'property': prop
        })
        