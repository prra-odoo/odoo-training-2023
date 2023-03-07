# -*- coding: utf-8 -*-
from odoo import http

class Academy(http.Controller):

    @http.route('/academy/<model("estate.property"):teacher>/', auth='public', website=True)
    def teacher(self, teacher):
        return http.request.render('Estate.index', {
        'person': teacher
    })
     
    #  @http.route('/academy/<name>/', auth='public', website=True)
    #  def teacher(self, name):
    #     return '<h1>{}</h1>'.format(name)
     
    #  @http.route('/property/', auth='public', website=True)
    #  def index(self, **kw):
    #      property = http.request.env['estate.property']
    #      return http.request.render('Estate.index', {
    #          'property': property.search([])
    #      })
     

    # def index(self, **kw):
    #     return  http.request.render('Estate.index',{
    #         'name' : ['astik','rohan','nisha','kiya']
    #     })                            





