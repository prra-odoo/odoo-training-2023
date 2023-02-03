# -*- coding: utf-8 -*-
from odoo import http,api

class real_estate(http.Controller):
    @http.route(['/estate/estate/','/estate/estate/page/<int:page>'],auth='public' ,website=True)
    def index(self,page=0,search='',**kw):
        domain=[]
        if search:
            domain.append(('name','ilike','search'))
        # Property =  http.request.env['estate.property']
        estates = http.request.env['estate.property'].search(domain)
        total_total = estates.sudo().search_count([])
        pager = http.request.website.pager(
            url='/estate/estate/',
            total = total_total,
            page=page,
            step=3,
            url_args=None,
        )
        package= http.request.env['estate.property'].search(domain,limit=4,offset=pager['offset'],order='id desc')
        return http.request.render('estate.index',{
            'properties' : package,
            'pager' : pager,
        })
    # @http.route('/estate/<name>/', auth='public', website=True)
    # def property(self, name):
    #     return '<h1>{}</h1>'.format(name)
    
    # @http.route('/estate/<int:id>/', auth='public', website=True)
    # def property(self, id):
    #     return '<h1>{} ({})</h1>'.format(id, type(id).__name__)
    
    @http.route('/estate/<model("estate.property"):properties>/',auth='public',website=True)
    def property(self,properties):
        return http.request.render('estate.template_controller',{
            'prop' : properties
        })  