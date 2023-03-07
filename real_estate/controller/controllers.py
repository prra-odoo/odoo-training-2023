from odoo import http

class Academy(http.Controller):

    @http.route('/academy/academy/', auth='public',website=True)
    def index(self, **kw):
        return http.request.render('real_estate.index', {
            'teachers': ["Diana Padilla", "Jody Caroll", "Lester Vaughn"],
        })