# -*- coding: utf-8 -*-

from odoo import http

class RealEstate(http.Controller):
    @http.route(['/estate/home', '/estate/home/page/<int:page>'],type="http" ,auth='public', website=True)
    def index(self, page=1, **kw):
        domain = [('state', 'in', ['new', 'offer_received'])]
        Properties = http.request.env['estate.property'].search(domain)
        total = Properties.search_count([])
        pager = http.request.website.pager(
            url='/estate/home',
            total=total,
            page=page,
            step=9
        )
        pagerProperties = Properties.search(domain,offset=(page - 1) * 9, limit=9)
        return http.request.render('real_estate.index', {
            'properties': pagerProperties,
            'pager':pager
        })
        

    # @http.route('/estate/<name>', auth='public', website=True)
    # def property(self, name):
    #     return '<h1>{}</h1>'.format(name)

    # @http.route('/estate/<int:id>', auth='public', website=True)
    # def property(self, id):
    #     return '<h1>{} ({})</h1>'.format(id, type(id).__name__)

    @http.route('/estate/<model("estate.property"):name>', auth='public', website=True)
    def property(self, name):
        return http.request.render('real_estate.property', {
            'properties': name
        })
