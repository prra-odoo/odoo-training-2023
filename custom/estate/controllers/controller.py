from odoo import http
class Estate(http.Controller):

    @http.route('/estate/estate/', auth='public')
    def index(self, **kw):
        Teachers = http.request.env['estate.property']
        return http.request.render('estate.index', {
            'teachers': Teachers.search([])
        })