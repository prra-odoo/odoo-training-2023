from odoo import http

class Controllers(http.Controller):

    @http.route(['/estate/estate','/estate/estate/page/<int:page>'],auth="public",website=True)
    def index(self,page=0, **kw):
        Properties = http.request.env['estate.property']
        total = Properties.sudo().search_count([])
        pager = http.request.website.pager(
            url='/estate/estate',
            total=total,
            page=page,
            step=4,
        )
        return http.request.render('estate.index', {
             'properties': Properties.search([('state','not in',('sold','canceled'))],limit=4,offset=pager['offset'],order='id desc'),
             'pager': pager,
        })
    
    @ http.route('/estate/estate/<model("estate.property"):property>/', auth = "public", website = True)
    def property_list(self, property):
        return http.request.render('estate.website_property_view', {
            'property': property,
        })