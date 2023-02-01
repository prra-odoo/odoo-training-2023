from odoo import http

class estateController(http.Controller):
    @http.route('/estate/estate/',auth='public',website=True)
    def controller_helloworld(self,**kw):
        # return "Hello world"
        # return http.request.render('estate.estate_controller_test',{
        #     'properties': ['estate1','estate2','estate3'],
        # })
        # adding the estate property model data
        Properties = http.request.env['estate.property']
        return http.request.render('estate.estate_controller_test',{
            'properties': Properties.search([])
        })
    # __ converter pattern __
    # @http.route('/estate/<name>' , auth= 'public' , website= True)
    # def controller_url_routing(self,name):
    #     return '<h1>{}</h1>'.format(name)

    # # restricting url to integr only
    # @http.route('/estate/<int:id>' , auth= 'public' , website= True)
    # def controller_url_routing(self,id):
    #     return '<h1>{}({})</h1>'.format(id,type(id).__name__)


    # making particular pages for the particular property
    @http.route('/estate/<model(estate.property):estate_property>/',auth = "public" , website = True)
    def controller_model(self,estate_property):
        return http.request.render('estate.listing_property',{
            'listed_property': estate_property
        })
  