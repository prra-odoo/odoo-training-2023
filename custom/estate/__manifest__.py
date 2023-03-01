# -- coding: utf-8 -
{
    'name': "Real Estate",
    'depends': ['base','mail'],
    'application': True,
    'data':[
        'security/ir.model.access.csv',

        'views/res_users.xml',
        'views/estate_property_offer.xml',
        'views/estate_property_views.xml',
        'views/estate_property_tags.xml',
        'views/estate_property_types.xml',
        'views/estate_menus.xml'
        
    ],
    'license':'LGPL-3',
    'demo':[
        'demo/estate_property_demo_data.xml',
    ]

    
}