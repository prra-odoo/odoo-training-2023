
from odoo import http


class Academy(http.Controller):

    @http.route('/academy/academy/', auth='public')
    def index(self, **kw):
         Teachers = http.request.env['estate.real.property']
         return http.request.render('estate.index', {
             'teachers': Teachers.search([])
         })
