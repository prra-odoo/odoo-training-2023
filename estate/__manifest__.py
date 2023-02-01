# -*- coding: utf-8 -*-

{
    'name': 'Real Estate',
    'summary': 'Module for Real Estate Advertising the property you hducc loiug',
    'description': """This Module help the user to completely make their real estate""",
    'author' : "Nishit Thakkar",
    'depends': ['base'],
    'category': 'Category',
    'installable': True,
    'application': True,
    'auto_install': False,
    'sequence':0,
    'data':[
        'security/ir.model.access.csv',
        'views/estate_menus.xml',
        'views/estate_property_views.xml',
        'views/estate_property_type.xml',
        'views/estate_property_tags.xml',
        'views/estate_property_offer.xml',
        'views/inherit_user.xml',
        ],
    'depends':['mail',],
    'demo':[
        'demo/estate_property_demo.xml',
    ],
    'icon':"estate/static/description/icon.png",
    'license': 'LGPL-3',
}