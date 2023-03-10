from odoo import http

class Estate(http.Controller):
    # for getting the all properties
    # @http.route('/estate/estate/', auth='public',website=True)
    # def index(self, **kw):
    #     Property= http.request.env['estate.property']
    #     return http.request.render('estate.index', {
    #         'property': Property.search([('state','not in',('sold','canceled'))])
    #     })
    


# limit is a parameter passed to the search method of the estate.property model.
# It specifies the maximum number of records that should be returned by the search query. In this case, limit is set to 4, which means that the search query will return a maximum of 4 estate properties.

# step is a parameter passed to the pager method of the http.request.website object.
# It specifies the number of items to display per page. In this case, step is also set to 4, which means that each page of results will display 4 estate properties.



# So, the main difference between limit and step is that limit controls the maximum number of items that 
# can be returned by the search query,whereas step controls the number of items displayed per page on the website.


    @http.route(['/estate/','/estate/page/<int:page>'], auth='public',website=True)
    def index(self,page=1,**kw):
        domain=[('state','not in',('sold','canceled'))]
        date= kw.get('date_picker')
        if(date):
            domain.append(('create_date','>=',date))
        Properties= http.request.env['estate.property'].search(domain,offset=(page-1)*3, limit=4)
        total = Properties.search_count([])
        pager = http.request.website.pager(
            url='/estate/',
            total = total,
            page = page,
            # step is used to determine the number of items to display per page. In this case, 
            # step is set to 4, which means that each page of results will display 4 estate properties.
            step=4
            )
        return http.request.render('estate.index', {
            'properties':Properties,
            'pager':pager,
                })
    

    @http.route('/estate/<model("estate.property"):prop>', auth='public', website=True)
    def property(self, prop):
        return http.request.render('estate.property_details_view',{
            'property' : prop
            })