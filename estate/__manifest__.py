# -*- coding: utf-8 -*-
{
    'name' : 'Real Estate',
    'description' : 'Real Estate Advertising Module',
    'application' : True, 
    'depends': ['base', 'mail'], 
    'data' : [
        'security/ir.model.access.csv',
        'views/estate_view.xml',
        'views/estate_view_action.xml',
        'views/estate_offer.xml',
    ],
    'demo' : [
        'demo/estate_demodata.xml',
    ],
}