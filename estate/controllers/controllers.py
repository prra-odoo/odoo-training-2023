# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class Estate(http.Controller):

    @http.route('/estate/estate/', auth='public', website=True)
    def index(self, **kw):
        Properties = http.request.env['estate.property']
        return http.request.render('estate.index', {
            'properties': Properties.search([])
        })

    @http.route('/estate/<model("estate.property"):property>/', auth='public', website=True)
    def teacher(self, property):
        return http.request.render('estate.description', {
        'property': property
    })
    
    # @http.route('/estate/<model("estate.property"):property>/', auth='public', website=True)
    # def teacher(self, property):
    #     Properties = http.request.env['estate.property']
    #     return http.request.render('estate.index', {
    #         'properties': Properties.search([])
    # })