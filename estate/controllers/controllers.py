# -*- coding: utf-8 -*-
from odoo import http

class Estate(http.Controller):
    # @http.route('/estate/estate',auth='public',website=True)
    # def index(self, **kw):
    #     estate = http.request.env['estate.property'].search([])
    #     return http.request.render('estate.index',{
    #         'estate':estate
    #     })

    # @http.route('/estate/<name>/', auth='public', website=True)
    # def teacher(self, name):
    #     return '<h1>{}</h1>'.format(name)

    # @http.route('/academy/<int:id>/', auth='public', website=True)
    # def student(self, id):
    #     return '<h1>{} ({})</h1>'.format(id, type(id))

    @http.route('/estate/<model("estate.property"):estate>/', auth='public', website=True)
    def teacher(self, estate):
        return http.request.render('estate.index', {
            'new': estate
        })