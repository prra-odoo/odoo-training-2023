# -*- coding: utf-8 -*-
{
    'name': "Real Estate"   , 
    'depends':['base','mail'], 
    'data':['security/ir.model.access.csv',
            'report/estate_property_templates.xml',
            'report/estate_property_reports.xml',
            'views/estate_offers_view.xml',
            'views/estate_property_views.xml',
            'views/estate_property_type_views.xml',
            'views/estate_property_tag.xml',
            'views/estate_menus.xml'
    ],
    'demo':[ 'demo/estate_demo_data.xml',
    ],

    'application': True,
    'license': 'LGPL-3',
    'images': ['static/description/icon.png']
}