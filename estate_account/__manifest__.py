# -*- coding: utf-8 -*-

{
    'name': 'Estate Account',
    'description': 'Real Estate Account',
    'version': '1.0',
    'sequence': 2,
    'category': 'Marketing',
    'author': 'Dhrutik Patel (dhrp)',
    'website': 'https://www.odoo.com/',
    'summary': 'Real Estate Account',
    'depends': ['real_estate','account'],
    'demo': [],
    'data': [
        'report/estate_property_offer_inherit.xml'
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
