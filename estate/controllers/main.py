# -*- coding: utf-8 -*

from odoo import http
from odoo.http import request  
from odoo.addons.portal.controllers.portal import pager as portal_pager


class EstatePropertycontroller(http.Controller):

    # @http.route('/estate/estate/',auth='public',website=True)
    # def propertyestate(self, **kw):
    #     properties = http.request.env['estate.property']
    #     return request.render("estate.property_controller_template",{
    #         'property' : properties.search([]),
    #     })

    @http.route(
        [
            '/estate/estate',
            '/estate/estate/page/<int:page>',
            '/estate/estate/type/<model("estate.property.type"):proptype>/'
        ]
            ,type='http',auth='public',website=True)
    def propertypager(self,page=0,search='',proptype=None):
        domain=[]
        if search:
            domain = [('name','ilike' , search)]
        total_properties = request.env['estate.property'].search(domain)
        total_count = len(total_properties)
        per_page = 4

        pager = request.website.pager(url='/estate/estate/',total=total_count,page=page,step=per_page,scope=3,url_args=None)
        eprop = request.env['estate.property'].search(domain,limit=per_page,offset=pager['offset'],order='id asc')

        if proptype:
            eprop = eprop.search([('property_type_id','in',[0,proptype.id])])
        groups = request.env['estate.property.type'].search([])

        if not proptype:
            proptype = request.env['estate.property.type']
            
        values = {
            'groups' : groups,
            'proptype' : proptype,
            'property' : eprop,
            'pager' : pager,
        }
        return request.render('estate.property_controller_template',values)

    @http.route('/estate/<model("estate.property"):prop>/',type='http', auth='public', website=True)
    def properties(self, prop):
        return request.render('estate.property_controller_template_redirect', {
            'about': prop
        })