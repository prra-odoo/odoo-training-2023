# -*- coding: utf-8 -*-
from odoo import http

class Estates(http.Controller):

    @http.route('/my_estate', auth='public',website=True)
    def index(self, **kw):
         EAgents = http.request.env['estate.controller.practice']
         return http.request.render('real_estate.index', {
             'teachers': EAgents.search([])
         })


    # # New route
    # @http.route('/my_estate/<int:id>/', auth='public', website=True)
    # def convertingb(self, id):
    #     print(id)
    #     print(type(id).__name__)
    #     return '<h1>{} ({})</h1>'.format(id, type(id).__name__)



    @http.route('/my_estate/<model("estate.controller.practice"):id>/', auth='public', website=True)
    def teacher(self, id):
        return http.request.render('real_estate.biography', {
            'person': id
        })



      