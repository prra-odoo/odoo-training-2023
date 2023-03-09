from odoo import http

class ControllerDemo(http.Controller):

    @http.route("/property",auth="public",website=True)
    def index(self,**kw):
        properties = http.request.env["estate.property"].search([('state','in',['new','offer received'])])
        if(len(properties) > 10):
            properties = properties[0:10:1]
            print("============================",properties)
        return http.request.render("estate.index",{
            "properties" : {
                "data" : properties,
                "id" : 1
            }
        })
    
    @http.route("/property/1",auth="public",website=True)
    def second_page(self,**kw):
        properties = http.request.env["estate.property"].search([('state','in',['new','offer received'])])
        if(len(properties) > 10):
            properties = properties[10::1]
        else:
            properties = []
        return http.request.render("estate.index",{
            "properties" : {
                "data" : properties,
                "id" : 2
            }
        })
    
    @http.route('/property/<model("estate.property"):property>/', auth='public', website=True)
    def about(self, property):
        return http.request.render('estate.about', {
            'property': property
        })