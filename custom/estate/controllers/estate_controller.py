from odoo import http

class Estate(http.Controller):
    @http.route(['/properties', '/properties/page/<int:page>'], auth='public', website=True)
    def index(self, page=1, **kw):
        Properties = http.request.env['estate.property']
        total_properties = Properties.search_count([])
        pager = http.request.website.pager(
                url='/properties/',
                total = total_properties,
                page=page,
                step=4,
                url_args=None,  
            )
        properties  = Properties.search([('state', 'in', ['new', 'offer received'])], limit=4, offset=pager['offset'])

        vals = {'properties': properties, 'pager': pager}    
         
        return http.request.render('estate.index', vals)
    
    @http.route('/properties/<model("estate.property"):property>/', auth='public', website=True)
    def property(self, property):
        return http.request.render('estate.property',{
            'properties': property
        })