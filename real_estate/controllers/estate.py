# -*- coding: utf-8 -*-
from odoo import http

class Estate(http.Controller):

    # rendering templates
    @http.route('/estate/property/', auth='public', website=True)
    def index(self, **kw):
        Property = http.request.env['estate.property']
        return http.request.render('real_estate.controller_estate_property', {
             'properties': Property.search([])
         })

    # rendering data from url
    @http.route('/home/<name>/<int:id>/', auth='public', website=True)
    def home(self, name, id):
        return '<h1>{} {} ({})</h1>'.format(name, id, type(id).__name__)

    # rendering from model
    @http.route('/estate/<model("estate.property"):property>/', auth='public', website=True)
    def estate(self, property):
        return http.request.render('real_estate.controller_estate_property_1', {
            'properties': property
        })
    