# -*- coding: utf-8 -*-

{
    'name' : 'RealEstate',
    'category' : "Real Estate/Brokerage",
    'summary' : 'Selling Your property',
    'description' : 'This app will help you to find the best deal for your properties',
    'version' : '1.0',
    'author' : 'THSH',
    'data' : [    
        'security/real_estate_security.xml',
        'security/ir.model.access.csv',
        'views/estate_menus.xml',
        'views/estate_property_offer.xml',
        'views/estate_property_views.xml',
        'views/estate_property_type.xml',
        'views/estate_property_tags.xml',
        'views/res_users_view.xml',
        # 'reports/offers_template.xml',
        'reports/estate_property_template.xml',
        'reports/property_user_template.xml',
        'reports/estate_property_report.xml',
        ],
    'demo' : [  
        'demo/estate_property_demo.xml',
        'demo/estate_property_type_demo.xml',
        'demo/estate_property_tag_demo.xml'
       ],
    'depends' : ['mail'],
    'installable' : True,
    'application' : True,
    'auto_install' : False
}