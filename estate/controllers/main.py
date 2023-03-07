# -*- coding: utf-8 -*-

from odoo import http

class Estate(http.Controller):
    @http.route('/estate',auth='public',website=True)
    def index(self, **kw):
        return http.request.render('estate.index',{
            'teachers' : ['Jay','Mayur','Naman']
        })