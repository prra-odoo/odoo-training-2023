# -*- coding: utf-8 -*-

from odoo import http
from odoo.addons.portal.controllers.portal import pager as portal_pager

class RealEstate(http.Controller):
    @http.route(['/estate/home', '/estate/home/page/<int:page>'],type="http" ,auth='public', website=True)
    def index(self, page=1, **kw):
        domain = [('state', 'in', ['new', 'offer_received'])]
        if kw.get('filterDate'):
            domain = ['&',('date_availability', '>', kw.get('filterDate')), ('state', 'in', ['new', 'offer_received'])]
        if kw.get('searchName'):
            domain = ['&',('name', 'ilike', kw.get('searchName')), ('state', 'in', ['new', 'offer_received'])]

        Properties = http.request.env['estate.property'].search(domain,offset=(page - 1) * 9, limit=9)
        total = Properties.search_count([])
        pager = portal_pager(
            url='/estate/home',
            total=total,
            page=page,
            url_args={'searchName': kw.get('searchName'),'filterDate':kw.get('filterDate')},
            step=9
        )
        return http.request.render('real_estate.index', {
            'properties': Properties,
            'pager':pager,
            'page':page
        })

    @http.route('/estate/<model("estate.property"):name>', auth='public', website=True)
    def property(self, name):
        return http.request.render('real_estate.property', {
            'properties': name
        })
