# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class Estate(http.Controller):

    @http.route(['/estate/estate/','/estate/estate/page/<int:page>'], auth='public', website=True)
    def index(self, page=0, search=''):
        domain = []
        if search:
            domain = [('name','ilike',search)]
        total = request.env['estate.property'].search(domain)
        total_count = len(total)
        per_page = 4

        pager = request.website.pager(url='/estate/estate',total=total_count, page=page,step=per_page,scope=3, url_args=None)
        Properties = request.env['estate.property'].search(domain,limit=per_page, offset=pager['offset'],order='id asc')
        return http.request.render('estate.index', {
            'properties': Properties,
            'pager': pager
        })

    @http.route('/estate/<model("estate.property"):property>/', auth='public', website=True)
    def teacher(self, property):
        return http.request.render('estate.description', {
        'property': property
    })
    
    # @http.route('/estate/<model("estate.property"):property>/', auth='public', website=True)
    # def teacher(self, property):
    #     Properties = http.request.env['estate.property']
    #     return http.request.render('estate.index', {
    #         'properties': Properties.search([])
    # })