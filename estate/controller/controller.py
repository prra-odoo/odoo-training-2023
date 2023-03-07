from odoo import http

class Controller(http.Controller):
    @http.route('/estate/estate/', auth='public')
    def index(self, **kw):
        return http.request.render('estate.index', {
            'teachers': ["Diana Padilla", "Jody Caroll", "Lester Vaughn"],
        })