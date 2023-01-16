# -*- coding: utf-8 -*-

{
    'name': "Real Estate",
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_type_views.xml',
        'views/estate_tag_views.xml',
        'views/estate_property_offers_views.xml',
        'demo/estate_property_demo_data.xml',
        'demo/estate_type_demo_data.xml',
        'demo/estate_tag_demo_data.xml',
        'views/estate_property_menus.xml',
    ],
    'author': "rare",
    'category': 'sales',
    'description': """
        This is my Real Estate Module.
        Created by rare!
    """,
    'installable': True,
    'application': True,
}