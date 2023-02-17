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
    def index(self, page=1, search='', **kw):
        domain = [('state', 'in', ['new', 'offer_received'])]
        if search:
            domain = [('name','ilike' , search)]
        Properties = http.request.env['estate.property'].search(domain)
        total = Properties.search_count([])

        date_availability = kw.get('date_availability')
        if date_availability:
            domain.append(('date_availability','>=', date_availability))

        pager = http.request.website.pager(
            url='/estate/estate',
            total=total,
            page=page,
            step=3
        )
        pagerProperties = Properties.search(domain,offset=(page - 1) * 4, limit=4)
        return http.request.render('estate.index', {
            'properties': pagerProperties,
            'pager':pager
        })