from odoo import http

class EstatePropertyController(http.Controller):

    @http.route('/estate/property/', auth='public', website=True)
    def index(self, **kw):
        property = http.request.env['estate.property']
        # return "Hello, world"
        return http.request.render('estate.estate_property_web_view',{
            'properties' : property.search([])
        })
