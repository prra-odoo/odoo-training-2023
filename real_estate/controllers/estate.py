# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers.portal import pager as portal_pager

class Estate(http.Controller):

    # rendering templates
    @http.route(['/estate/property','/estate/property/page/<int:page>'], method=['GET'], type="http", auth='public', website=True)
    def index(self, page=1, **kw):
        date = kw.get('date')
        print(date)
        Property = http.request.env['estate.property'].search([])
        total = Property.search_count([])
        pager = portal_pager(
                    url='/estate/property',
                    total=total,
                    page=page,
                    step=5,
                )
        response_property = Property.search(([]),limit=5, offset=pager['offset'])

        return http.request.render('real_estate.controller_estate_property', {
             'properties': response_property.sudo(),
             'pager':pager
         })

    # rendering data from url
    @http.route('/home/<name>/<int:id>', auth='public', website=True)
    def home(self, name, id):
        return '<h1>{} {} ({})</h1>'.format(name, id, type(id).__name__)

    # rendering from model
    @http.route('/estate/<model("estate.property"):property>',auth='public', website=True)
    def estate(self, property):
       
        return http.request.render('real_estate.controller_estate_property_1', {
            'property': property,
        })

    # @http.route('/estate/<name>', type='http', methods=['GET'], auth="public", website=True, csrf=False)
    # def test_path(self, name, **kw):
    #     #here in kw you can get the inputted value
    #     print("---------------------------------------------------------",name)