from odoo import http

class EstateController(http.Controller):
    @http.route('/estate',auth='public',website=True)
    def index(self,**kw):
        return http.request.render('real_estate.index',{
            'properties':http.request.env['real.estate.property'].search([])
        })
    @http.route('/estate/<model("real.estate.property"):property>/',auth='public',website=True)
    def teacher(self,property):
        return http.request.render('real_estate.property_view',{
            'property':property
        })