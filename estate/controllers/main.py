from odoo import http

class Estate(http.Controller):

    @http.route('/estate/estate/', auth='public',website=True)
    def index(self, **kw):
        
        properties= http.request.env['estate.property']
        return http.request.render('estate.report_property_offers',{
            'docs': properties.search([])
        })
    

     