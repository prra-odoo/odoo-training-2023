from odoo.http import request
from odoo import http

class Estate(http.Controller):
    

  #for search...
     @http.route(['/estate/estate/','/estate/estate/page/<int:page>'], auth='public', website=True)
     def index(self, page=0, search=''):
        domain = []
        if search:
            domain = [('name','ilike',search)]
        total = http.request.env['estate.property'].search(domain)
        total_count = len(total)
        per_page = 4

        pager = request.website.pager(url='/estate/estate',total=total_count, page=page,step=per_page,scope=3, url_args=None)
        Properties = http.request.env['estate.property'].search(domain,limit=per_page, offset=pager['offset'],order='id asc')
        return http.request.render('real_estate.index', {
            'properties': Properties,
            'pager': pager
        })

     @http.route('/estate/<model("estate.property"):property>/', auth='public', website=True)
     def teacher(self, property):
        return http.request.render('real_estate.description', {
        'property': property
    })

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
    #  @http.route('/estate/estate/', type="http", auth="public", website=True)
    
    #  def index(self, **kw):
    #     estate_property = http.request.env['estate.property'].sudo().search([])
    #     data = {
    #         'records': estate_property
    #     }
    #     return http.request.render("real_estate.demo_controller_template", data)
    
    # ROUTE 4
    #  @http.route('/estate/<model("estate.property"):property>/', auth='public', website=True)
    
    #  def estate(self, property):
    #     return http.request.render('real_estate.single_property_template', {'record': property})
