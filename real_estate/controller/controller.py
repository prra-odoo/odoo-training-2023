# -*- coding: utf-8 -*-
from odoo import http


class Controller(http.Controller):

    # @http.route('/controller/controller/', auth='public')
    # def index(self, **kw):
    #     return "Hello, Dhrumil"

    @http.route(['/controller/controller/', '/controller/controller/page/<int:page>'], auth='public', website=True)
    def index(self, page=1, **kw):
        domain = []

        Property = http.request.env['real.estate'].search(domain,offset=(page-1)*6,limit=6)
        total=Property.search_count([])
        pager= http.request.website.pager(
            url='/controller/controller/',
            total=total,
            page=page,
            step=3,
        )
        return http.request.render('real_estate.property_view', {
            'properties': Property,
            'pager':pager, 
        })

    @http.route('/controller/<model("real.estate"):estate>/', auth='public', website=True)
    def property_list(self, estate):
        return http.request.render('real_estate.property_list_view', {
            'person': estate
        })
