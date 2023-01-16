# -*- coding: utf-8 -*-
{
    'name': "Real Estate",
    'version': '1.0',
    'category': "Category",
    'summary': 'Manage Property Related Offers and more',
    'description': "Real Estate module",
    'author': "Raj Patani",
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_menus.xml',
    ],
    'demo': [
        'demo/real_estate_demo_data.xml'
    ],
    'sequence' :-100,
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}