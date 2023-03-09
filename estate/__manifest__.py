{
    'name': "real estate",
    'depends': ['base','mail','website'],
    'application': True,
    'license':'LGPL-3',
    'data':[
        'security/ir.model.access.csv',
        
        'views/estate_property_views.xml',
        'views/estate_property_offer_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',
        'controller/template.xml',
        'controller/controller_view.xml',
        'views/inherit_user_views.xml',
        'views/estate_menus.xml',
        'report/estate_property_reports.xml',
        'report/estate_property_templates.xml',
        
    ],
    'demo':[
        'demo/estate_property_demo.xml',
    ]
}