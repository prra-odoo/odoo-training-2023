# -- coding: utf-8 -
{
    'name': "Real Estate",
    'depends': ['base','mail','website'],
    'application': True,
    'category': 'Real Estate/Brokerage',
    'data':[
        'controllers/template.xml',
        
        'security/security.xml',
        
        'security/ir.model.access.csv',
        'report/estate_property_reports.xml',
        'report/estate_property_templates.xml',
        
        
        'views/res_users.xml',
        'views/estate_property_offer.xml',
        'views/estate_property_views.xml',
        'views/estate_property_tags.xml',
        'views/estate_property_types.xml',
        'views/estate_menus.xml',
        
        
    ],
    'license':'LGPL-3',
    'demo':[
        'demo/estate_property_demo_data.xml',
    ]

    
}