# -*- coding: utf-8 -*-
{
    'name' : 'Real Estate',
    'description' : 'Real Estate Advertising Module',
    'category': 'Real Estate/Brokerage',
    'application' : True, 
    'depends': ['base', 'mail'], 
    'data' : [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/estate_menu.xml',
        'views/estate_view.xml',
        'views/estate_offer.xml',
        'views/estate_type.xml',
        'views/estate_tags.xml',
        'views/res_users.xml',
    ],
    'demo' : [
        'demo/estate_demodata.xml',
    ],
    'license': 'LGPL-3',
}
