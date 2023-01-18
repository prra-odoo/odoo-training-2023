{
    'name': 'real_estate',
    'version': '1.0',
    'category': 'Marketing',
    'summary': 'Find rates of real estates',
    'description': "App for Real Estate management",
    'author': 'sami',
    'data': [
        'security/ir.model.access.csv',
        'views/real_estate_menu.xml',
        'views/estate_property_views.xml',
        'views/estate_property_offer.xml',
        'views/estate_property_type.xml',
        'views/estate_property_tag.xml',
        

    ],
    'demo': [
        'demo/estate_property_demo.xml',
        'demo/estate_property_type_demo.xml',
        'demo/estate_property_tag_demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False

}