# -*- coding: utf-8 -*-
from odoo import http

class Controllers(http.Controller):

    @http.route('/academy/academy/', auth='public',website = True)
    def index(self):
        return "Hello, world"
    