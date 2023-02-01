from requests import request
from odoo import http

class Estate(http.Controller):
    @http.route('/estate/estate/', auth='public', website=True)
    def index(self, **kw):
        Properties = http.request.env['estate.property']
        return http.request.render('real_estate.index', {
            'properties': Properties.search([])
        })

    @http.route('/estate/<model("estate.property"):property>/', auth='public', website=True)
    def route(self, property):
        return http.request.render('real_estate.route', {
        'Propertie': property
    })

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
