# -*- coding: utf-8 -*-

{
    'name': 'Real Estate',
    'description': 'The Real Estate Advertisement module',
    'version': '1.0',
    'category': 'Marketing',
    'author': 'Dhrutik Patel (dhrp)',
    'website': 'https://www.odoo.com/',
    'summary': 'The Real Estate Advertisement module',
    'depends': [],
    'demo': [
        'demo/estate_property_tag_demo.xml',
        'demo/estate_property_type_demo.xml',
        'demo/estate_property_demo.xml',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_offer.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',
        'views/estate_property_views.xml',
        'views/estate_menus.xml',
    ],
    'installable': True,
    'application': True,
}
