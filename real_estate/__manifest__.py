# -*- coding: utf-8 -*-
{
    'name' : 'Real_Estate',
    'author': "Ravi Bhingradiya",
    'depends': ['mail'],
    'data' : [
            'security/ir.model.access.csv',
            'views/estate_menus.xml',
            'views/estate_property_view.xml',
            'views/estate_property_type_view.xml',
            'views/estate_property_offer_view.xml',
            'views/res_users_view.xml',
            
    ],

    'demo' : [ 
            'data/real_estate_demo_data.xml'
    ],
    'application' : True,
    'installable': True,
    'license': 'LGPL-3',
}