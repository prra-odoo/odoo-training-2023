from odoo import http

class EstateController(http.Controller):
    @http.route(['/estate/','/estate/page/<int:page>',],auth='public',website=True)
    def index(self,page=1,**kw):
        domain=[]
        if kw.get('availability_date'):
            domain.append(('date_availability','=',kw.get('availability_date')))
        model_ids = http.request.env['real.estate.property'].search(domain, offset=(page - 1) * 5, limit=5)
        total=model_ids.search_count([])
        pager=http.request.website.pager(
            url='/estate',
            total=total,
            page=page,
            step=5
        )
        
        return http.request.render('real_estate.index',{
            
            'properties':model_ids,'pager':pager,'description_hide':kw.get('description_hide'),'page':page
        })
    @http.route('/estate/<model("real.estate.property"):property>/',auth='public',website=True)
    def propertyDetail(self,property):
        
        return http.request.render('real_estate.property_view',{
            'property':property
        })