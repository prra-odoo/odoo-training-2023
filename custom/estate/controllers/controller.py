
from odoo import http


class Controller(http.Controller):
   
    @http.route(['/properties/','/properties/page/<int:page>/'], auth='public', website=True)
    def index(self,page=0,search='', **kw):
        
        domain=[]
        if search:
            domain.append(('name','ilike',search))
        
        Teachers = http.request.env['estate.real.property'].search(domain)
       
        total_total = Teachers.sudo().search_count([])
        pager = http.request.website.pager(
            url='/properties/',
            total = total_total,
            page=page,
            step=3,
            url_args=None,
        )
        package = http.request.env['estate.real.property'].search(domain,limit=3,offset=pager['offset'],order='id desc')
        return http.request.render('estate.index',{
            # 'teachers': Teachers.search([('state', 'in', ['new', 'recieved'])]),
            'teachers' : package,
            'pager' : pager,
        })

    @http.route('/properties/<model("estate.real.property"):teacher>/',auth="public",website=True)
    def property(self, teacher):
        return http.request.render('estate.index_template', {
             'properties': teacher
        })
    
   
    
   
    
    
    
    





