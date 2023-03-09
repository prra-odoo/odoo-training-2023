from odoo import http

class Estate(http.Controller):
    # for getting the all properties
    # @http.route('/estate/estate/', auth='public',website=True)
    # def index(self, **kw):
    #     Property= http.request.env['estate.property']
    #     return http.request.render('estate.index', {
    #         'property': Property.search([('state','not in',('sold','canceled'))])
    #     })
    



    @http.route(['/estate/','/estate/page/<int:page>'], auth='public',website=True)
    def index(self,page=1,**kw):
        domain=[('state','not in',('sold','canceled'))]
        Properties= http.request.env['estate.property'].search(domain,offset=(page-1)*3, limit=3)
        total = Properties.search_count([])
        pager = http.request.website.pager(
            url='/estate/',
            total = total,
            page = page,
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