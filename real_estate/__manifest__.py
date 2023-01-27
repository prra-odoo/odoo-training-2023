# -*- coding: utf-8 -*-

{
    'name': 'Real Estate',
    'description': 'The Real Estate Advertisement module',
    'version': '1.0',
    'sequence': 1,
    'category': 'Marketing',
    'author': 'Dhrutik Patel (dhrp)',
    'website': 'https://www.odoo.com/',
    'summary': 'The Real Estate Advertisement module',
    'depends': ['mail'],
    'demo': [
        'demo/estate_property_tag_demo.xml',
        'demo/estate_property_type_demo.xml',
        'demo/estate_property_demo.xml',
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/estate_sold_property_views.xml',
        'views/estate_property_offer.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',
        'views/estate_property_views.xml',
        'views/res_users_inherited_views.xml',
        'views/estate_menus.xml',
    ],
    'category': 'Real Estate/Brokerage',
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
