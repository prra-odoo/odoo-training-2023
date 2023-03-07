# -*- coding: utf-8 -*-
from odoo import http

class EstateController(http.Controller):

    @http.route('/estate', auth='public',website=True)
    def index(self, **kw):
        Properties = http.request.env['estate.property']
        return http.request.render('estate.index', {
            'properties':Properties.search([])
        })