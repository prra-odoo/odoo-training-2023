from odoo import http

class Estate(http.Controller):
    @http.route(['/estate','/estate/page/<int:page>'],auth='public',website=True)
    def index(self,page=1,**kw):
        data=http.request.env["estate.property"]
        total=data.search_count([])
        pager=http.request.website.pager(
            url='/estate/',
            total = total,
            page=page,
            step=10,
            url_args=None,

        )
        prop=data.search([],offset=pager['offset'], limit=10)
        return http.request.render('estate.index', {
            'es_data': prop,
            'pager':pager

        })  
    #  def index(self, page=1, **kw):
    #     domain = []
    #     property = http.request.env["estate.property"].search(domain,offset=(page-1)*6, limit=6)
    #     total = property.search_count([])
    #     pager = http.request.website.pager(
    #         url='/real_estate/properties/',
    #         total=total,
    #         page=page,
    #         step=3,
    #     )
    #     return http.request.render('real_estate.property_list', {
    #         'properties': property,
    #         'pager': pager,
    #     })
    
    @http.route('/estate/<model("estate.property"):property>/',auth='public',website=True)
    def property(self,property):
        return http.request.render('estate.page',{
            'data':property
        })