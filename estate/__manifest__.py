# -- coding: utf-8 --
{
	'name': "Real Estate",
	'depends': ['base',],
	'data':[
		'security/ir.model.access.csv',
		'views/estate_property_views.xml',
		'views/estate_property_type_views.xml',
		'views/estate_property_tags_views.xml',
		'views/estate_property_offers_views.xml',
		'views/estate_menus.xml'
		],
	'image':['static/description/icon.png'],	
	
	'application': True,
	'license': 'LGPL-3',
}
