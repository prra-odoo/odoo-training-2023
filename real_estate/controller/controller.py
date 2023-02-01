from odoo import http

class RealEstate(http.Controller):

    @http.route('/real_estate', auth='public', website=True)
    def index(self, **kw):
        categories = http.request.env['estate.category']
        return http.request.render('real_estate.view', {
            'categories': categories.search([])
        }
        )