# -*- coding: utf-8 -*-
from odoo import http,api

class RealEstate(http.Controller):

    @http.route(['/estate/models/'], auth='public', website=True)
    def index(self,**kw):
        
        estate = http.request.env['estate.property']
        
        return http.request.render('estate.index',{
            'estate': estate.search([])
            })



    
  