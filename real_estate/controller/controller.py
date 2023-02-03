from odoo import http# defining controller for the estate properties
from odoo.addons.portal.controllers.portal import pager

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
    @http.route(['/real_estate/', '/real_estate/page/<int:page>'], type="http", auth="public", website=True)
    def index(self, page=1, items_per_page = 16, **kw):
        domain = []
        properties = http.request.env['estate.property'].search(domain)
        total = properties.search_count(domain)
        
        pagination = pager(
            url='/real_estate/',
            total=total,
            page=page,
            step=items_per_page
        )
        new_properties = properties.search(domain,limit=items_per_page, offset=pagination['offset'])
        return http.request.render('real_estate.real_estate_web_view', {
            'properties': new_properties,
            'pager': pagination,
        }
        )
    
    @http.route('/real_estate/<model("estate.property"):properties>', auth="public", website=True)
    def slug_def(self, properties):
        return http.request.render('real_estate.web_view_estate_page', {
            'property': properties,
        })