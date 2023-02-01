# -*- coding: utf-8 -*-
from odoo import http

class Academy(http.Controller):

     @http.route('/realestate/user/', auth='public',website=True)
     def index(self, **kw):
         property = http.request.env['estate.property']
         return http.request.render('real_estate.index', {
             'estates': property.search([])
         }) 

    
     @http.route('/realestate/<model("estate.property"):estate>/', auth='public', website=True)
     def estate(self, estate):
        return http.request.render('real_estate.detail', {
            'person': estate
        })