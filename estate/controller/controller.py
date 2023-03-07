from odoo import http

class Estate(http.Controller):

    @http.route('/estate/estate/', auth='public')
    def index(self, **kw):
        Property= http.request.env['estate.property']
        return http.request.render('estate.properties', {
            'property': Property.search([])
        })