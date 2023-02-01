# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class realEstateController(http.Controller):

    @http.route('/real_estate/models', auth='public', website=True)
    def index(self, **kw):
        property = http.request.env["estate.property"]
        return http.request.render('real_estate.property_list', {
            'properties': property.search([])
        })

    # @http.route('/academy/<name>/', auth='public', website=True)
    # def name(self, name):
    #     return '<h1>{}</h1>'.format(name)

    # @http.route('/real_estate/<estate.property("real_estate.properties"):property>/', auth='public', website=True)
    # def teacher(self,):
    #     return http.request.render('.biography', {
    #         'person':
    #     })
