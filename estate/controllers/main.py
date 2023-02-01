# -*- coding: utf-8 -*

from odoo import http
from odoo.http import request   

class EstatePropertycontroller(http.Controller):

    @http.route('/estate/estate',auth='public',website=True)
    def propertyestate(self, **kw):
        properties = http.request.env['estate.property']
        return request.render("estate.property_controller_template",{
            'property' : properties.search([]),
        })

    @http.route('/estate/<model("estate.property"):prop>/',type='http', auth='public', website=True)
    def properties(self, prop):
        return request.render('estate.property_controller_template_redirect', {
            'about': prop
        })



        