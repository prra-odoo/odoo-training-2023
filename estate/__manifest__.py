# -*- coding: utf-8 -*-
{
    'name': "Real Estate"   , 
    'depends':['base',], 
    'data':['security/ir.model.access.csv',
            'views/estate_offers_view.xml',
            'views/estate_property_views.xml',
            'views/estate_property_type_views.xml',
            'views/estate_property_tag.xml',
            'views/estate_menus.xml'
            
    ],
    
    'application': True,
    'license': 'LGPL-3',
    'images': ['static/description/icon.png']
}