# -*- coding: utf-8 -*-

from odoo import http


class EstateWeb(http.Controller):

    # @http.route('/estate/<model("estate.property"):properties', auth='public', website=True)
    # def index(self, properties):
    #     return http.request.render('estate.index', {
    #         'prop': properties
    #     })

    @http.route('/estate/', auth='public', website=True)
    def index(self, **kw):
        Properties = http.request.env['estate.property']
        return http.request.render('estate.index', {
            'properties': Properties.search([])
        })
