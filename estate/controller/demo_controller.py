# -*- coding: utf-8 -*
from odoo import http


class estate_property(http.Controller):

    @http.route('/estate', auth='public',website=True)
    def index(self, **kw):
        Properties = http.request.env['estate.property']
        return http.request.render('estate.estate_property', {
            'properties': Properties.search([]),
        })

    # @http.route('/estate/', auth='public', website=True)
    # def index(self, **kw):
    #     Teachers = http.request.env['estate.property']
    #     return http.request.render('estate.index', {
    #         'teachers': Teachers.search([])
    #     })