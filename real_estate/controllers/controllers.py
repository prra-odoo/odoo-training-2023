from odoo import http
from odoo.http import request
from odoo.tools import is_html_empty


class RealEstate(http.Controller):
    
    @http.route(['/real_estate','/real_estate/page/<int:page>'], type='http', auth="public", website="True")
    def estate_property(self , page=1,item_per_page=8, **post):
        # return "Hello, world"
        property_data = request.env['real.estate.property']
        total = property_data.search_count([])
        pager = request.website.pager(url='/real_estate',total=total ,page=page,step=9,scope=10)
        domain=[('state' ,'not in', ['sold','canceled'])]
        date_availability = post.get('date_availability')
        if date_availability:
            domain.append(('date_availability', '>' ,date_availability))
        prop_data = property_data.search(domain,limit=9, offset=pager['offset'])
        return request.render('real_estate.property_list', {'records': prop_data,'pager': pager,'is_html_empty': is_html_empty})
    
    @http.route('/real_estate/<model("real.estate.property"):property>/', auth='public', website=True)
    def EstatePropertyDetail(self, property):
        return request.render('real_estate.property_data',{'records':property})
    
    # def estate_property_view(self, page=0, **post):
    #     model_ids = request.env['real.estate.property'].search([], offset=(page - 1) * 10, limit=5)
    #     total = model_ids.search_count([])
    #     pager = request.website.pager(url='/real_estate',total=total,page=page,step=3,)
    #     return request.render('real_estate.property_list', {'records': prop_data,'pager': pager,'is_html_empty': is_html_empty})