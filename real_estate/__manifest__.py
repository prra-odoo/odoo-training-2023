{
    'name': 'Real Estate',
    'version': '1.0',
    'category': 'Marketing',
    'depends':[
        'calendar',
        'contacts',
       ],
    'author': 'Archana',
    'summary': 'Track estate properties',
    'description': 'Real estate module',
    'installable': True,
    'application': True,
    'data':[
         'security/ir.model.access.csv',
         'views/estate_property_actions.xml',
         'views/estate_property_menu.xml',
         'views/estate_property_views.xml',
         'data/estate_property_data.xml',
         'data/estate_property_type_data.xml',
         'data/estate_property_tag_data.xml',
         'views/estate_property_type_view.xml',
         'views/estate_property_tags_view.xml',
         'views/estate_property_offer_view.xml',
    ]
}