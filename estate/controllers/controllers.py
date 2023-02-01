# -*- coding: utf-8 -*-
from odoo import http

class Estate(http.Controller):

    @http.route('/estate/estate/', auth='public', website=True)
    def index(self, **kw):
        Property = http.request.env['estate.property']
        return http.request.render('estate.index', {'properties': Property.search([])})

    @http.route('/estate/<model("estate.property"):property>/', auth='public', website=True)
    def property(self, property):
        return http.request.render('estate.listing', {'plot': property})
