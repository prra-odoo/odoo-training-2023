# -*- coding: utf-8 -*-
{
    'name': 'Real Estate',
    'author': 'KASP',
    'depends': [
        'base',
    ],
    'data': [
        'security/ir.model.access.csv',

        'views/estate_property_views.xml',
        'views/estate_property_type_view.xml',
        'views/estate_menu.xml',
    ],
    'application': True,
    'installable': True,
    'license': 'LGPL-3',
}
