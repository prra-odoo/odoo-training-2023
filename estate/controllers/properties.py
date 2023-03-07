from odoo import http

class Properties(http.Controller):

    @http.route('/properties/', auth='public', website=True)
    def index(self, **kw):
        Properties = http.request.env['estate.property']
        return http.request.render('estate.properties_template', {
            'properties': Properties.search([('state','in',['new','offer received']),('active','=',True)])
        })