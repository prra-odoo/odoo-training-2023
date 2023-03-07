from odoo import http

class Estate(http.Controller):
    @http.route('/properties', auth='public', website=True)
    def index(self):
        Properties = http.request.env['estate.property']
        return http.request.render('estate.index', {
            'properties': Properties.search([('state', 'in', ['new', 'offer received'])])
        })