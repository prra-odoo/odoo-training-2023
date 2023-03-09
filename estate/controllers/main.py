from odoo import http



class Estate(http.Controller):

    @http.route('/estate/estate/', auth='public',website=True)
    def index(self, **kw):
        
        properties= http.request.env['estate.property']
        return http.request.render('estate.report_property_offers',{
            'docs': properties.search([])
        })

    @http.route('/property/<model("estate.property"):property>/',auth='public',website=True)
    def property(self,property):
        return http.request.render('estate.property_details',{
            'docs':property
        })

   
    @http.route(['/property/','/property/page/<int:page>'], auth='public', website=True)
    def index(self,page=0,search='', **kw):
        domain=[]
        if search:
            domain.append(('name','ilike',search))
        Properties = http.request.env['estate.property'].search(domain)
        total_properties = Properties.sudo().search_count([])
        pager = http.request.website.pager(
            url='/property/',
            total = total_properties,
            page=page,
            step=4,
            url_args=None,
        )
        package = http.request.env['estate.property'].search(domain,limit=4,offset=pager['offset'],order='id desc')
        return http.request.render('estate.property_website_template',{
            'properties' : package,
            'pager' : pager,
        })


      
        