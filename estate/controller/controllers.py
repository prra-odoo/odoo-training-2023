# -- coding: utf-8 --
from odoo import http

class Controllers(http.Controller):

    @http.route(['/properties/','/properties/page/<int:page>'], auth='public', website=True)
    def index(self,page=0,search='', **kw):
        domain=[('state', 'in', ['new','offer received'])]
        if search:
            domain.append(('name','ilike',search))
        Properties = http.request.env['estate.property'].search(domain)
        total_properties = Properties.sudo().search_count([])
        pager = http.request.website.pager(
            url='/properties/',
            total = total_properties,
            page=page,
            step=4,
            url_args=None,
        )
        package = http.request.env['estate.property'].search(domain,limit=4,offset=pager['offset'],order='id desc')
        return http.request.render('estate.properties_template',{
            'properties' : package,
            'pager' : pager,
        })

    @http.route('/properties/<model("estate.property"):properties>/',auth='public',website=True)
    def property(self,properties):
        return http.request.render('estate.template_controller',{
            'prop' : properties
        })