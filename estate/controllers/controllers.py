from odoo import http

class Controllers(http.Controller):
   
    @http.route(['/estate/estate','/estate/estate/page/<int:page>'],auth="public",website=True)
    def index(self,page=0, **kw):
        # domain=[]
        # if search:
        #     domain.append(('name','ilike',search))

         
        Properties = http.request.env['estate.property']
        total_properties = Properties.sudo().search_count([])
        pager = http.request.website.pager(
            url='/estate/estate',
            total = total_properties,
            page=page,
            step=4,
            url_args=None,
        )
        Properties = http.request.env['estate.property'].search([('state','=','new')],limit=4,offset=pager['offset'],order='id desc')



        return http.request.render('estate.index', {
             'properties':Properties,
            #  'properties': Properties.search([('state','not in',['sold'])])
             'pager' : pager,

        })



    # @http.route(['/properties/','/properties/page/<int:page>'], auth='public', website=True)
    # def index(self,page=0,search='', **kw):
    #     domain=[]
    #     if search:
    #         domain.append(('name','ilike',search))
    #     Properties = http.request.env['estate.property'].search(domain)
    #     total_properties = Properties.sudo().search_count([])
    #     pager = http.request.website.pager(
    #         url='/properties/',
    #         total = total_properties,
    #         page=page,
    #         step=4,
    #         url_args=None,
    #     )
    #     package = http.request.env['estate.property'].search(domain,limit=4,offset=pager['offset'],order='id desc')
    #     return http.request.render('estate.properties_template',{
    #         'properties' : package,
    #         'pager' : pager,
    #     })






    @http.route('/estate/<model("estate.property"):property>/',auth="public",website=True)
    def property(self, property):
        return http.request.render('estate.property_template', {
             'properties': property
        })






