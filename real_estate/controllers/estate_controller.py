# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request

class EstateController(http.Controller):
    @http.route('/estate-property/', type="http", auth="public")
    
    def index(self, **kw):
        estate_property = request.env['estate.property'].sudo().search([])
        data = {
            'records': estate_property
        }
        return request.render("real_estate.estate_property_controller_template", data)