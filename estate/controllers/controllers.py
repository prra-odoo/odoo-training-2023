from odoo import http

class Properties(http.Controller):

	@http.route(['/properties','/properties/page/<int:page>'], auth='public', website=True)
	def index(self,page=1, *kw):
		domain=[('state','not in',['sold','canceled'])]
		Properties = http.request.env['estate.property'].search(domain,offset=(page-1)*3, limit=3)
		total = Properties.search_count([])
		pager = http.request.website.pager(
			url='/properties',
			total=total,
			page=page,
			step=3,
	)
		return http.request.render('estate.index',{
			'properties' : Properties,
			'pager': pager,
			})

	@http.route('/properties/<model("estate.property"):prop>', auth='public', website=True)
	def property(self, prop):
		return http.request.render('estate.property_details_view',{
    		'property' : prop
    		})