from odoo import http

class Estate(http.Controller):
    @http.route('/estate', auth='public',website=True)
    def index(self, **kw):
        data=http.request.env["estate.property"]
        return http.request.render('estate.index', {
            'es_data': data.search([])
        })

