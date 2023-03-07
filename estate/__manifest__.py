# -*- coding: utf-8 -*-
{
    'name': 'Real Estate',
    'author': 'KASP',
    'category': 'Real Estate/Brokerage',
    'depends': [
        'base',
        'mail',
        'website',
    ],
    'application': True,
    'installable': True,
    'license': 'LGPL-3',
    'image': ['static/description/icon.png'],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/estate_property_offer.xml',
        'views/estate_property_type_view.xml',
        'views/estate_property_tag.xml',
        'report/estate_property_templates.xml',
        'report/estate_property_reports.xml',
        'views/demo_templates.xml',
        'views/estate_property_views.xml',
        'views/estate_menu.xml',
    ],
    'demo': [
        'demo/estate_demo_data.xml',
    ]
}
