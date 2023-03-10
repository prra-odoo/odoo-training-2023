# -*- coding: utf-8 -*-
from odoo import http


class Estate(http.Controller):

    @http.route('/properties', auth='public', website="true")
    def index(self, **kw):
        estate_property_req_obj = http.request.env['estate.property']
        # estate.index --> moduleName.template id
        return http.request.render('estate.index', {
            'property_list': estate_property_req_obj.search([])
            # this "property_list" is then used in the templates.xml
        })

    # New route

    # @http.route('/academy/<name>/', auth='public', website=True)
    # def teacher(self, name):
    #     return '<h1>{}</h1>'.format(name)

    # @http.route('/academy/<int:id>/', auth='public', website=True)
    # def teacher(self, id):
    #     return '<h1>{} ({})</h1>'.format(id, type(id).__name__)

    @http.route('/properties/<model("estate.property"):property>/', auth='public', website=True)
    def teacher(self, property):
        return http.request.render('estate.biography', {
            'property': property
        })
