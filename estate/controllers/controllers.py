# -*- coding: utf-8 -*-
from odoo import http
from odoo.addons.portal.controllers.portal import pager as portal_pager

class Estate(http.Controller):
    @http.route(['/estate', '/estate/page/<int:page>'],auth='public',website=True)
    def index(self,page=1,**kw):
        date = kw.get('date')
        search = kw.get('search')
        domain = []
        if date:
            domain.append(('date_availability','>',date))
        elif search != '':
            domain.append(('name','ilike',search))
        else:
            pass
        usr = http.request.env['res.users'].browse(http.request.env.uid)
        if usr.has_group('estate.estate_group_user'):
            domain.append(('website_published','=',True))

        estate = http.request.env['estate.property'].search(domain,offset=(page-1)*6, limit=6)
        total = estate.search_count([])
        pager = portal_pager(
            url="/estate",
            url_args={'search': search,'date':date},
            total=total,
            page=page,
            step=3
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