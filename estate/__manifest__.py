# -*- coding: utf-8 -*-
{
    'name': 'Real Estate',
    'author': 'KASP',
    'depends': [
        'base',
        'mail',
    ],
    'application': True,
    'installable': True,
    'license': 'LGPL-3',
    'image': ['static/description/icon.png'],
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_property_offer.xml',
        'views/estate_property_type_view.xml',
        'views/estate_property_tag.xml',
        'views/estate_menu.xml',
    ],
    'demo': [
        'demo/estate_demo_data.xml',
    ]
}
