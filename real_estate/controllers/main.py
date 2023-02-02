from odoo import http

class Realestate(http.Controller):

    @http.route('/real_estate', auth='public',website="True")
    def index(self, **kw):
        properties = http.request.env['real.estate.properties']
        return http.request.render('real_estate.index', {
            'properties': properties.search([])
        })

    # @http.route('/real_estate/<model("real.estate.properties"):properties>/', auth='public',website="True")
    # def estateindex(self, properties):
    #     return http.request.render('real_estate.index', {'properties': properties})

    @http.route('/real_estate/<model("real.estate.properties"):properties>/', auth='public',website="True")
    def estateindexdata(self, properties):
        return http.request.render('real_estate.property_data', {'properties': properties})