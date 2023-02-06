# -*- coding: utf-8 -*-
from odoo import http
from odoo.addons.portal.controllers.portal import pager as portal_pager

class Estate_web(http.Controller):
    
    @http.route(['/estate/home','/estate/home/page/<int:page>'],type="http" ,auth='public', website=True)
    
    def pagin(self, page=1,item_per_page=8,**kw):
        
        domain = [('state', 'in', ['new', 'offer_received'])]
        Properties = http.request.env['estate.property.model'].search(domain)
        total = Properties.search_count(domain)
        
        pager = portal_pager(
            url='/estate/home',
            total=total,
            page=page,
            step=item_per_page
        )
        response_property = Properties.search(domain,limit=item_per_page, offset=pager['offset'])

        return http.request.render('real_estate.mainp', {
            'properties': response_property.sudo(),
            'pager':pager
        })


    @http.route('/estate/home/<model("estate.property.model"):id>',auth='public',website=True)
    def index(self, id):
        return http.request.render('real_estate.desp',{
            'property': id
        })
    
  