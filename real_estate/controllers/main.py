from odoo import http

class Realestate(http.Controller):

    # @http.route('/real_estate', auth='public',website="True")
    # def index(self, **kw):
    #     properties = http.request.env['real.estate.properties']
    #     return http.request.render('real_estate.index', {
    #         'properties': properties.search([])
    #     })

    # @http.route('/real_estate/<model("real.estate.properties"):properties>/', auth='public',website="True")
    # def estateindex(self, properties):
    #     return http.request.render('real_estate.index', {'properties': properties})


    @http.route('/real_estate/<model("real.estate.properties"):properties>/', auth='public',website="True")
    def estateindexdata(self, properties):
        return http.request.render('real_estate.property_data', {'properties': properties})

    @http.route(['/real_estate', '/real_estate/page/<int:page>'], type="http", auth="public", website=True) 
    def index(self, page=1, items_per_page=8, **kw): 
        domain = [('state' ,'not in',('sold','canceled'))]

        date = kw.get('available_date')
        if date:
            domain.append(('date_availability', '>=', date))

        estate_property = http.request.env['real.estate.properties'] 
        estate_property_count = estate_property.search_count (domain)


        pager = http.request.website.pager( 
            url="/real_estate",
            total=estate_property_count,
            page=page,
            step=items_per_page
        )
        response_property = estate_property.search(domain,limit=items_per_page, offset=pager['offset']) 

        data = { 
            'properties': response_property.sudo (), 
            'pager': pager, 
            } 
        return http.request.render("real_estate.index", data)