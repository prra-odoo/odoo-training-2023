# -*- coding: utf-8 -*-

from odoo import http
from odoo.addons.portal.controllers.portal import pager as portal_pager


class RealEstate(http.Controller):
    @http.route(['/estate/home','/estate/home/page/<int:page>'],type="http" ,auth='public', website=True)
    
    def index(self, page=1,item_per_page=8,**kw):
        
        domain = [('state', 'in', ['new', 'offer_received'])]
        Properties = http.request.env['estate.property'].search(domain)
        total = Properties.search_count(domain)
        
        pager = portal_pager(
            url='/estate/home',
            total=total,
            page=page,
            step=item_per_page
        )
        response_property = Properties.search(domain,limit=item_per_page, offset=pager['offset'])

        return http.request.render('real_estate.index', {
            'properties': response_property.sudo(),
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
