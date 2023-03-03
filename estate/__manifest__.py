# -- coding: utf-8 --
{
	'name': "Real Estate",
	'depends': ['base','mail'],
	'data':[
		'security/ir.model.access.csv',
		'views/estate_property_offers_views.xml',
		'views/estate_property_tags_views.xml',
		'views/estate_property_type_views.xml',
		'report/estate_property_reports.xml',
		'report/estate_property_templates.xml',
		'views/estate_property_views.xml',
		'views/estate_menus.xml'
		],
	'image':['static/description/icon.png'],
	'demo': [
        'demo/estate_property_demo_data.xml'	
		],
	'application': True,
	'license': 'LGPL-3',
}
