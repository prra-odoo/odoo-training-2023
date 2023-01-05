# -*- coding: utf-8 -*-

{
    'name': "Real Estate",
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_menus.xml',
        'views/estate_type_views.xml'
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