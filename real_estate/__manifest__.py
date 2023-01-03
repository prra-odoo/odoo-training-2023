# -*- coding: utf-8 -*-

{
    'name': "Real Estate",
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_menus.xml'
    ],
    'author': "rare",
    'category': 'sales',
    'description': """
        This is my Real Estate Module.
        Created by rare!drop
    """,
    'installable': True,
    'application': True,
}