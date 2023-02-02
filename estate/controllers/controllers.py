# -*- coding: utf-8 -*-
from odoo import http

class Estate(http.Controller):

    @http.route('/estate/estate/', auth='public', website=True)
    def index(self, **kw):
        Property = http.request.env['estate.property']
        return http.request.render('estate.index', {'properties': Property.search([])})


    @http.route('/estate/<model("estate.property"):property>/', auth='public', website=True)
    def property(self, property):
        return http.request.render('estate.listing', {'plot': property})

    @http.route(['/estate/estate', '/estate/estate/page/<int:page>'],type="http" ,auth='public', website=True)
    def index(self, page=1, **kw):
        domain = [('state', 'in', ['new', 'offer_received'])]
        Properties = http.request.env['estate.property'].search(domain)
        total = Properties.search_count([])
        pager = http.request.website.pager(
            url='/estate/estate',
            total=total,
            page=page,
            step=3
        )
        pagerProperties = Properties.search(domain,offset=(page - 1) * 9, limit=10)
        return http.request.render('estate.index', {
            'properties': pagerProperties,
            'pager':pager
        })