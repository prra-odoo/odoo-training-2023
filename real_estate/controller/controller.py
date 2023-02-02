from odoo import http

class RealEstate(http.Controller):

    # @http.route('/real_estate/', auth='public', website=True)
    # def index(self, **kw):
    #     categories = http.request.env['estate.category']
    #     return http.request.render('real_estate.view', {
    #         'categories': categories.search([])
    #     }
    #     )

    # # @http.route('/real_estate/<name>/', auth='public', website=True)
    # # def index(self, name):
    # #     return f'<h1>{name}</h1>'

    # @http.route('/real_estate/<model("estate.category"):categories>', auth='public', website=True)
    # def index1(self, categories):
    #     return http.request.render('real_estate.description', {
    #         'category': categories,
    #     }
    #     )

    # defining controller for the estate properties
    @http.route('/real_estate/', auth="public", website=True)
    def index(self, **kw):
        properties = http.request.env['estate.property']
        return http.request.render('real_estate.real_estate_web_view', {
            'properties': properties.search([])
        }
        )
    
    @http.route('/real_estate/<model("estate.property"):properties>', auth="public", website=True)
    def slug_def(self, properties):
        return http.request.render('real_estate.web_view_estate_page', {
            'property': properties,
        })