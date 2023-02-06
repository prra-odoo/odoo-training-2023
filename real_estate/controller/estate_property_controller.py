# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class estatePropertyController(http.Controller):

    @http.route(['/real_estate/properties/', '/real_estate/properties/page/<int:page>'], auth='public', website=True)
    def index(self, page=1, **kw):
        domain = []
        property = http.request.env["estate.property"].search(domain,offset=(page-1)*6, limit=6)
        total = property.search_count([])
        pager = http.request.website.pager(
            url='/real_estate/properties/',
            total=total,
            page=page,
            step=3,
        )
        return http.request.render('real_estate.property_list', {
            'properties': property,
            'pager': pager,
        })

    @ http.route('/real_estate/<model("estate.property"):property>/', auth = "public", website = True)
    def property_list(self, property):
        return http.request.render('real_estate.property_list_view', {
            'estate': property
        })
