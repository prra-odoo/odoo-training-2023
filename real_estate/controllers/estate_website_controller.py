# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request
# from odoo.addons.portal.controllers.portal import pager as portal_pager

class EstateWebsiteController(http.Controller):
    # ROUTE 1
    # @http.route('/estate/<name>/', auth="public", website=True)
    
    # def index(self, name):
    #     return '<h1>Good Afternoon {}</h1>'.format(name)
    
    # ROUTE 2
    # @http.route('/estate/<int:id>/', auth="public", website=True)
    
    # def index(self, id):
    #     return '<h1>Good Afternoon {}</h1>'.format(id)
    
    # ROUTE 3
    @http.route(['/estate/estate/', '/estate/estate/page/<int:page>'], type="http", auth="public", website=True)
    
    def index(self, page=1, items_per_page=8, **kw):
        
        domain=[('state', 'not in', ['sold', 'cancelled'])]
        
        estate_property = request.env['estate.property']
        estate_property_count = estate_property.search_count(domain)
        
        date_availability = kw.get('date_availability')
        if date_availability:
            domain.append(('date_availability','>=', date_availability))
            
        # pager
        pager = request.website.pager(
        url="/estate/estate",
        total=estate_property_count,
        page=page,
        step=items_per_page
        )
        # content according to pager
        response_property = estate_property.search(domain, limit=items_per_page, offset=pager['offset'])
        
        data = {
            'records': response_property.sudo(),
            'pager': pager,
            
        }
        return request.render("real_estate.estate_property_list_controller_template", data)
    
    # ROUTE 4
    @http.route('/estate/<model("estate.property"):property>/', auth='public', website=True)
    
    def estate(self, property, **kw):
        is_visible = True
        
        if kw.get('btn-hide'):
            is_visible = False

        return http.request.render('real_estate.single_property_template', {'record': property, 'is_visible': is_visible})