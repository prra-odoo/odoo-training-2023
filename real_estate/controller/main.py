# -*- coding: utf-8 -*-
from odoo import http

class Realestate(http.Controller):

    # @http.route('/realestate', auth='public',website="True")
    # def index(self, **kw):
    #     properties = http.request.env['real.estate.properties']
    #     return http.request.render('real_estate.index', {
    #         'properties': properties.search([])
    #     })

    @http.route('/estate/<model("real.estate.properties"):property>/', auth='public', website=True)
    def estate(self, property):
       return http.request.render('real_estate.details', {
            'properties': property
    })



    @http.route(['/realestate', '/realestate/page/<int:page>'], type="http", auth="public", website=True) 
    def index(self, page=1, items_per_page=10, **kw): 

        estate_property = http.request.env['real.estate.properties'] 
        estate_property_count = estate_property.search_count ([]) 
        pager = http.request.website.pager( 
            url="/realestate",
            total=estate_property_count,
            page=page,
            step=items_per_page
        )
        response_property = estate_property.search([],limit=items_per_page, offset=pager['offset']) 
        
        data = { 
            'properties': response_property.sudo (), 
            'pager': pager, 
            } 
        return http.request.render("real_estate.index", data)

    # @http.route('/realestate/id', auth='public',website="True")
    # def index(self, id):
    #     return '<h1>{}</h1>'.format(id)

    # @http.route('/realestate/<int:id>', auth='public',website="True")
    # def index(self, id):
    #     return '<h1>{}</h1>'.format(id)

    # @http.route('/properties', auth='public', website=True)
    # def ind(self, **kw):
    #     Properties = http.request.env['real.estate.properties']
    #     return http.request.render('real_estate.index', {
    #         'properties': Properties.search([])
    #     })

    