# -*- coding: utf-8 -*-
from odoo import http

class Estate(http.Controller):
    @http.route(['/estate', '/estate/page/<int:page>'], auth='public', website=True)
    def index(self,page=1,**kw):
        domain = [('website_published','=',True)]
        estate = http.request.env['estate.property'].search(domain,offset=(page-1)*6, limit=6)
        total = estate.search_count([])
        pager = http.request.website.pager(
            url='/estate',
            total=total,
            page=page,
            step=3,
        )
        return http.request.render('estate.home', {
            'estate': estate,
            'pager':pager,
        })

    @http.route('/estate/<model("estate.property"):estate>/', auth='public', website=True)
    def teacher(self, estate):
        return http.request.render('estate.index', {
            'new': estate
        })
