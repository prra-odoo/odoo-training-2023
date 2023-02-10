# -*- coding: utf-8 -*-
{
    'name': "Real Estate",
    'version': '1.0',
    'category': "Real Estate/Brokerage",
    'summary': 'Manage Property Related Offers and more',
    'description': "Real Estate module",
    'author': "Raj Patani",
    'depends': ['mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_property_offer.xml',
        'views/estate_property_type.xml',
        'views/estate_property_tag.xml',
        'views/inherited_res_user_views.xml',
        'views/estate_menus.xml',
    ],
    'demo': [
        'demo/real_estate_property_tags_demo_data.xml',
        'demo/real_estate_property_type_demo_data.xml',
        'demo/real_estate_demo_data.xml',
    ],
    'sequence' :-100,
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}