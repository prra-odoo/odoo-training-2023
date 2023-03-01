{
    'name': "real estate",
    'depends': ['base','mail'],
    'application': True,
    'license':'LGPL-3',
    'data':[
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/inherit_user_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',
        'views/estate_property_offer_views.xml',
        
        'views/estate_menus.xml'
    ],
    'demo':[
        'demo/estate_property_demo.xml',
    ]
}