from odoo import http
from odoo.addons.portal.controllers.portal import pager as portal_pager

class estateController(http.Controller):
    # @http.route('/estate/estate/',auth='public',website=True)
    # def controller_helloworld(self,**kw):
    #     # return "Hello world"
    #     # return http.request.render('estate.estate_controller_test',{
    #     #     'properties': ['estate1','estate2','estate3'],
    #     # })
    #     # adding the estate property model data
    #     Properties = http.request.env['estate.property']
    #     return http.request.render('estate.estate_controller_test',{
    #         'properties': Properties.search([])
            
    #     })
    @http.route(['/estate/estate', '/estate/estate/page/<int:page>'],type="http" ,auth='public', website=True)
    def index(self, page=1, search='',**kw):
        filter_date = kw.get('date')
        domain = [('state', 'in', ['new', 'offer_recieved'])]
        if filter_date:
            domain = ['&',('state', 'in', ['new', 'offer_recieved']),('date_availability','>',filter_date)]

       
        if search:
            domain= ['&',('state','in',['new','offer_recieved']),('name','ilike',search)]
        
        Properties = http.request.env['estate.property'].search(domain)
        total = Properties.search_count([])
        pager = portal_pager(
            url='/estate/estate',
            total=total,
            page=page,
            url_args = {'date':filter_date},
            step=1
        )
        
        pagerProperties = Properties.search(domain,offset=(page - 1) * 10, limit=10)
        return http.request.render('estate.estate_controller_test', {
            'properties': pagerProperties,
            'pager':pager,
            'page':page
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

  