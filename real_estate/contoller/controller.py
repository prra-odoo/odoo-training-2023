from requests import request
from odoo import http

class Estate(http.Controller):
     @http.route('/estate/estate/', type="http", auth="public", website=True)
    
     def index(self, **kw):
        estate_property = http.request.env['estate.property'].sudo().search([])
        data = {
            'records': estate_property
        }
        return http.request.render("real_estate.demo_controller_template", data)
    
    # ROUTE 4
     @http.route('/estate/<model("estate.property"):property>/', auth='public', website=True)
    
     def estate(self, property):
        return http.request.render('real_estate.single_property_template', {'record': property})

    #route for pager
    #  @http.route(['/customer', '/customer/page/<int:page>'], type="http", auth="public", website=True)
    #  def customer_kanban(self, page=0, search='', **post):
    #     domain = []
    #     if search:
    #         domain.append(('name', 'ilike', search))
    #     if search:
    #         post["search"] = search
    #         customer_obj = request.env['estate.property'].sudo().search(domain)
    #         total = customer_obj.sudo().search_count([])
    #     pager = request.website.pager(
    #     url='/customer',
    #     total=total,
    #     page=page,
    #     step=3,
    #         )




    #  @http.route('/academy/academy/', auth='public', website=True)
    #  def index(self, **kw):

    #     property = http.request.env['estate.property'].search([('state','in',('new','sold'))])
    #     # print(property)        
    #     return http.request.render('real_estate.index', {
    #          'property': property,
    #     })

    #  @http.route('/academy/<model("estate.property"):property>/', auth='public', website=True)
    #  def property(self, property):
    #       return http.request.render('real_estate.index', {
    #            'property': property,
    #       })

        # @http.route('/academy/<name>/', auth='public', website=True)
        # def teacher(self, name):
        #     return '<h1>{}</h1>'.format(name)
        # @http.route('/academy/<int:id>/', auth='public', website=True)
        # def teacher(self, id):
        #     return '<h1>{} ({})</h1>'.format(id, type(id).__name__)

        # @http.route('/academy/<model("estate.property"):property>/', auth='public', website=True)
        # def property(self, property):
        #     return http.request.render('real_estate.name', {
        #          'property': property,
        #     })
    #  @http.route('/academy/<model("estate.property"):property>/', auth='public', website=True)
