# -*- coding: utf-8 -*-
from odoo import http

class EstateController(http.Controller):
        @http.route(['/estate','/estate/page/<int:page>'], auth='public', website=True)
        def prop(self,page=1,search="", **kw):
            domain=[('state','in',['new','offer_received'])]
            if (search):
                 domain.append(('name','ilike',search))
            Properties = http.request.env['estate.property'].search(domain,offset=(page-1)*10, limit=10)
            total = Properties.search_count(domain)
            pager = http.request.website.pager(
                url='/estate',
                total=total,
                page=page,
                step=10,
            )
            return http.request.render('estate.properties',{
                'properties' : Properties,
                'pager':pager,
            })
        
        @http.route('/estate/<model("estate.property"):property>', auth='public', website=True)
        def index(self, property):
            return http.request.render('estate.property_details_view',{
                'property': property
            })        