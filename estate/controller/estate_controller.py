# -*- coding: utf-8 -*-

from odoo import http

class Estate(http.Controller):
    @http.route('/estate', auth='public', website=True)
    def index(self, **kw):
        Property = http.request.env['estate.property']
        return http.request.render('estate.index', {
            'properties': Property.search([])
        })
    # @http.route('/estate', auth='public')
    # def index(self, **kw):
    #     return http.request.render('estate.index', {
    #         'properties': ["Ghar 1", "Ghar 2", "Ghar 3"],
    #     })
    # @http.route('/estate', auth='public')
    # def index(self, **kw):
    #     return "Hello, world"

    # @http.route('/estate/<model("estate.property"):property>/', auth='public',website="True")
    # def estateindexdata(self, properties):
    #     return http.request.render('estate.property', {'property': property})

    # @http.route(['/estate', '/estate/page/<int:page>'], type="http", auth="public", website=True) 
    # def index(self, **kw): 
    #     domain = [('state' ,'not in',('sold','canceled'))]

    #     date = kw.get('available_date')
    #     if date:
    #         domain.append(('date_availability', '>=', date))

    #     estate_property = http.request.env['estate.property'] 
    #     estate_property_count = estate_property.search_count (domain)


    #     pager = http.request.website.pager( 
    #         url="/estate",
    #         total=estate_property_count,
    #         page=page,
    #         step=items_per_page # @http.route('/estate', auth='public')
    # def index(self, **kw):
    #     return "Hello, world"
    #     )
    #     response_property = estate_property.search(domain,limit=items_per_page, offset=pager['offset']) 

    #     data = { 
    #         'property': response_property.sudo (), 
    #         'pager': pager, 
    #         } 
    #     return http.request.render("estate.index", data)
