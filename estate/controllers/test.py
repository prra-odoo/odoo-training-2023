from odoo import http

class test(http.Controller):
    
    @http.route('/test',website = True)
    def testFun(self):
        properties = http.request.env['estate.property']
        return http.request.render('estate.test',{
            'prop': properties.search([])
            })