# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import http
from odoo.http import request

class Estate(http.Controller):

    # @http.route('/estate/estate/', auth='public')
    # def index(self, **kw):
    #     return http.request.render('real_estate.index',{
    #             'properties': ["Sea-facing appartment", "Odoo Office", "Mannat"],
    #     })

    # @http.route('/estate/estate/', auth='public',website=True)
    # def index(self, **kw):
    #     Properties=http.request.env['estate.properties']
    #     return http.request.render('real_estate.index',{
    #             'properties': Properties.search([])
    #     })

    # New route
    # @http.route('/estate/<int:id>/', auth='public', website=True)
    # def property(self, id):
    #     return '<h1>{}</h1>'.format(id,type(id).__name__)
    @http.route('/estate/<model("estate.properties"):property>/', auth='public', website=True)
    def estate(self, property):
       return http.request.render('real_estate.details', {
            'properties': property
    })

    @http.route(['/estate/estate/', '/estate/estate/page/<int:page>'], type="http", auth="public", website=True)

    def index(self, page=1, items_per_page=3, **kw):

        domain=[('state', 'not in', ['sold', 'cancelled'])]

        estate_property = request.env['estate.properties']
        estate_property_count = estate_property.search_count(domain)

        # pager
        pager = request.website.pager(
        url="/estate/estate",
        total=estate_property_count,
        page=page,
        step=items_per_page
        )
        # content according to pager
        response_property = estate_property.search([], limit=items_per_page, offset=pager['offset'])

        data = {
            'properties': response_property.sudo(),
            'pager': pager,
        }
        return request.render("real_estate.index", data)