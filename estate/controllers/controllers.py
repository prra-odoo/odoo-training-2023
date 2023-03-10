from odoo import http

class Controllers(http.Controller):
   
    @http.route(['/estate/estate','/estate/estate/page/<int:page>'],auth="public",website=True)
    def index(self,page=0, **kw):
        listed_after_date=kw.get('listed_after_date')

        domain=[('state','in',('new','cancelled'))]
        if (listed_after_date):
            domain.append(('create_date','>=',listed_after_date))

         
        Properties = http.request.env['estate.property']
        total_properties = Properties.sudo().search_count([])
        pager = http.request.website.pager(
            url='/estate/estate',
            total = total_properties,
            page=page,
            step=4,
            url_args=None,
        )
        Properties = http.request.env['estate.property'].search(domain,limit=4,offset=pager['offset'],order='id desc')
        
               
 
        return http.request.render('estate.index', {
             'properties':Properties,
             'pager' : pager,

        })





    @http.route('/estate/<model("estate.property"):property>/',auth="public",website=True)
    def property(self, property):
        return http.request.render('estate.property_template', {
             'properties': property
        })






