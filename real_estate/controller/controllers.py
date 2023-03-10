from odoo import http

class Estate(http.Controller):

    @http.route(['/estate/estate/','/estate/estate/page/<int:page>'], auth='public',website=True)
    def index(self,page=0, **kw):
        
        Property= http.request.env['estate.property']
        domain = [('state','not in',('sold','canceled'))]
        date= kw.get('date_picker')
        if(date):
            domain.append(('create_date','>=',date))
        total=Property.sudo().search_count([])
        pager = http.request.website.pager(
        url='/estate/estate/',
        total=total,
        page=page,
        step=3,
        )

        return http.request.render('real_estate.index', {
            'property': Property.search(domain,limit=3,offset=pager['offset'],order='id desc'),
            'pager': pager,
        })

    @ http.route('/estate/estate/<model("estate.property"):property>/', auth = "public", website = True)
    def property_list(self, property):
        return http.request.render('real_estate.website_view',{
            'properties': property,
        })