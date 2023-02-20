# -- coding: utf-8 --
from odoo import http

class Academy(http.Controller):

    @http.route('/properties', auth='public',website="True")
    def index(self, **kw):
         Properties = http.request.env['estate.property']
         return http.request.render('estate.index', {
             'properties': Properties.search([])
             })