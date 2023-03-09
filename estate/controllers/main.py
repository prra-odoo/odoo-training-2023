# -*- coding: utf-8 -*-

from odoo import http

class Estate(http.Controller):
    @http.route(['/estate', '/estate/page/<int:page>'],auth='public',website=True)
    def index(self,page=1, **kw):
        domain = [('state', 'in', ['new', 'offer_received'])]
        Properties = http.request.env['estate.property'].search(domain,offset=(page-1)*3, limit=3)
        total = Properties.search_count([])
        pager = http.request.website.pager(
            url='/estate',
            total=total,
            page=page,
            step=3,
        )
        return http.request.render('estate.index',{
            'properties' : Properties,
            'pager':pager,
        })

    @http.route('/estate/<model("estate.property"):property>', auth='public', website=True)
    def property(self, property):
        return http.request.render('estate.listing', {'plot': property})