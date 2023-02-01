# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import http

class Estate(http.Controller):

    # @http.route('/estate/estate/', auth='public')
    # def index(self, **kw):
    #     return http.request.render('real_estate.index',{
    #             'properties': ["Sea-facing appartment", "Odoo Office", "Mannat"],
    #     })

    @http.route('/estate/estate/', auth='public',website=True)
    def index(self, **kw):
        Properties=http.request.env['estate.properties']
        return http.request.render('real_estate.index',{
                'properties': Properties.search([])
        })