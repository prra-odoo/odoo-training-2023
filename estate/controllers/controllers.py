from odoo import http

class ControllerDemo(http.Controller):

    @http.route("/property",auth="public",website=True)
    def index(self,**kw):
        properties = http.request.env["estate.property"]

        return http.request.render("estate.index",{
            "properties" : properties.search([])
        })