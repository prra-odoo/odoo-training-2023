# -*- coding: utf-8 -*-
from odoo import http
from odoo.addons.portal.controllers.portal import pager as portal_pager

class Academy(http.Controller):

     @http.route(['/realestate/property/', '/realestate/property/page/<int:page>'],auth='public',website=True)
     def index(self,page=1,item_per_page=8,**kw):
        domain = [('state', 'in', ['new', 'offer_recieved'])]
        property = http.request.env['estate.property'].search(domain)
        total = property.search_count(domain)
        pager = portal_pager(
            url='/realestate/property',
            total=total,
            page=page,
            step=item_per_page
        )
        response_property = property.search(domain,limit=item_per_page, offset=pager['offset'])
        return http.request.render('real_estate.index', {
             'estates': response_property.sudo(),
             'pager':pager
         }) 

    
     @http.route('/realestate/<model("estate.property"):estate>/', auth='public', website=True)
     def estate(self, estate):
        return http.request.render('real_estate.detail', {
            'person': estate
        })