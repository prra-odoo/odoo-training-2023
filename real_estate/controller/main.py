# -*- coding: utf-8 -*-
from odoo import http

# class real_estate(http.Controller):

#     @http.route('/estate/properties/',auth='public',website="True")
#     def index(self, **kw):
#         properties = http.request.env['real.estate.properties']
#         return http.request.render('real_estate.index', {
#              'Properties': properties.search([])
#         })

class Realestate(http.Controller):

    @http.route('/realestate/realestate/', auth='public',website="True")
    def index(self, **kw):
        properties = http.request.env['real.estate.properties']
        return http.request.render('real_estate.index', {
            'properties': properties.search([])
        })







        