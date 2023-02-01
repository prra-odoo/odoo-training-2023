
# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class Academy(http.Controller):

    @http.route('/estate/estate/',website=True, auth='public')
    def index(self, **kw):
        # return "Hello, world"
        properties = http.request.env['estate.property']
        return http.request.render('real_estate.website_page_test', {
             'properties': properties.search([])
        })
        # return http.request.render('real_estate.website_page_test',{})