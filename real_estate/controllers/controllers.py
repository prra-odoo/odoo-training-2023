from odoo import http
from odoo.http import request
from odoo.tools import is_html_empty


class RealEstate(http.Controller):
    
    @http.route(['/real_estate','/real_estate/page/<int:page>'], type='http', auth="public", website="True")
    def estate_property(self , page=1 , **post):
        # return "Hello, world"
        # domain=[('state' ,'not in', ['sold','canceled'])]
        domain = []
        property_data = request.env['real.estate.property']
        if post.get('availability_date'):
            domain.append(('date_availability', '>' ,post.get('availability_date')))
        total = property_data.search_count(domain)
        pager = request.website.pager(url='/real_estate',total=total ,page=page,step=9,scope=10)
        prop_data = property_data.search(domain,limit=9, offset=pager['offset'])
        return request.render('real_estate.property_data', {'records': prop_data,'page':page,'description_hide':post.get('description_hide'),'pager': pager,'is_html_empty': is_html_empty})
    
    @http.route('/real_estate/<model("real.estate.property"):property>/', auth='public', website=True)
    def EstatePropertyDetail(self, property):
        return request.render('real_estate.property_detail',{'records':property})
    
    # def estate_property_view(self, page=0, **post):
    #     model_ids = request.env['real.estate.property'].search([], offset=(page - 1) * 10, limit=5)
    #     total = model_ids.search_count([])
    #     pager = request.website.pager(url='/real_estate',total=total,page=page,step=3,)
    #     return request.render('real_estate.property_list', {'records': prop_data,'pager': pager,'is_html_empty': is_html_empty})