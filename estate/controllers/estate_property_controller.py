from odoo import http

class EstatePropertyController(http.Controller):

    # @http.route(['/estate','/estate/page/<int:page>'], auth='public', website=True)
    # def index(self, page=1):
    #     property = http.request.env['estate.property']
    #     property_count = property.search_count([])

    #     pager = http.request.website.pager(
    #         url = '/estate',
    #         total = property_count,
    #         page=page,
    #         step=3
    #     )


    #     # return "Hello, world"
    #     return http.request.render('estate.estate_property_web_view',{
    #         'properties' : property.search([]),
    #         'pager' : pager
    #     })

    @http.route('/estate/properties/<model("estate.property"):property>', auth='public', website=True)
    def index(self, property, **kw):          
        
        return http.request.render('estate.property_details',{
            'property' : property
        })
    
    @http.route(['/estate', '/estate/page/<int:page>'], type="http", auth="public", website=True) 
    def index(self, page=1, items_per_page=3, **kw): 
        domain = [('state' ,'not in',('sold','canceled'))]
        name = kw.get('search_name')
        date = kw.get('search_date')
        if (name):
            domain.append(('name','like',name))
        if (date):
            domain.append(('date_availability','>=',date))
        property = http.request.env['estate.property'] 
        property_count = property.search_count ([])

        pager = http.request.website.pager( 
            url="/estate",
            total=property_count,
            page=page,
            step=items_per_page
        )
        print(pager)
        print('------------------',domain,'------------------')
        response_property = property.search(domain,limit=items_per_page, offset=pager['offset']) 
        print(len(property.search(domain)))
        print(len(response_property))
        # breakpoint()
        data = { 
            'properties': response_property, 
            'pager': pager, 
            
            } 
        return http.request.render("estate.estate_property_web_view", data)
