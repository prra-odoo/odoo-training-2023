from odoo import http
from odoo.http import request


class RealEstate(http.Controller):
    
    @http.route('/real_estate', type='http', auth="public", website="True")
    def estate_property(self, **post):
        # return "Hello, world"
        prop_data = request.env['real.estate.property'].search([])
        return request.render('real_estate.property_list', {'records': prop_data})
    
    @http.route('/real_estate/<model("real.estate.property"):property>/', auth='public', website=True)
    def EstatePropertyDetail(self, property):
        return request.render('real_estate.property_data',{'records':property})