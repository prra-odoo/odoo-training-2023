from odoo import http

class Properties(http.Controller):

    # @http.route('/properties', auth='public', website=True)
    # def index(self, **kw):
    #     Properties = http.request.env['estate.property']
    #     return http.request.render('estate.properties_template', {
    #         'properties': Properties.search([('state','in',['new','offer received','offer accepted']),('active','=',True)])
    #     })

    @http.route(['/properties','/properties/page/<int:page>'], auth='public', website=True)
    def index(self,page=0,search='', **kw):
        domain=[('state','in',['new','offer received','offer accepted']),('active','=',True)]
        if search:
            domain.append(('name','ilike',search))
        Properties = http.request.env['estate.property'].search(domain)
        total_properties = Properties.sudo().search_count([])
        pager = http.request.website.pager(
            url = '/properties',
            total = total_properties,
            page = page,
            step = 3,
            url_args = None,
        )
        package = http.request.env['estate.property'].search(domain,limit=3,offset=pager['offset'],order='id desc')
        return http.request.render('estate.properties_template',{
            'properties' : package,
            'pager' : pager,
        })

    @http.route('/properties/<model("estate.property"):properties>/',auth='public',website=True)
    def property(self,properties):
        return http.request.render('estate.template_controller',{
            'property' : properties
        })