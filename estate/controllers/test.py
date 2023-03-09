from odoo import http

class test(http.Controller):
    
    @http.route('/test/',website = True)
    def testFun(self):
        properties = http.request.env['estate.property']
        return http.request.render('estate.test',{
            'prop': properties.search([])
            })
    
    @http.route('/test/<model("estate.property"):x>/', auth='public', website=True)
    def teacher(self, x):
        return http.request.render('estate.test1', {
            'props': x
        })
    
    @http.route(['/test/','/test/page/<int:page>'], auth='public', website=True)
    def index(self,page=0,search='', **kw):
        domain=[]
        if search:
            domain.append(('name','ilike',search))
        Properties = http.request.env['estate.property'].search(domain)
        total_properties = Properties.sudo().search_count([])
        pager = http.request.website.pager(
            url='/test/',
            total = total_properties,
            page=page,
            step=4,
            url_args=None,
        )
        package = http.request.env['estate.property'].search(domain,limit=4,offset=pager['offset'],order='id desc')
        return http.request.render('estate.test',{
            'prop' : package,
            'pager' : pager,
        })