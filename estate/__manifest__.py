# -*- coding: utf-8 -*-
{
    'name': ' Real estate',
    'category': 'Real Estate/Brokerage',
    'summary': ' For buying and selling proerties.',
    'description': ' This is a  real estate Module',
    'author': 'Karnav',
    'depends' : ['mail'],
    'sequence': 1,
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/estate_menu.xml',
        'views/estate_property_view.xml',
        'views/estate_property_type_view.xml',
        'views/estate_property_tag.xml',
        'views/estate_property_offer.xml',
        'views/res_users_view.xml',
    ],
    'demo':[
        'demo/estate_property_tag_demo.xml',
        'demo/estate_property_type_demo.xml',
        'demo/estate_property_demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
