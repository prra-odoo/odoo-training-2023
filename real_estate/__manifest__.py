# -*- coding: utf-8 -*-

{
    'name' : 'Real Estate',
    'author' : 'Dhrumil Shah',
    'depends' : ['base','mail','account'],
    'version' : '1.0',
    'category' : 'Real Estate/Brokerage',
    'data': [
        'security/estate_security_rules.xml',
        'security/ir.model.access.csv',
        'views/view_estate_model.xml',
        'views/action_estate_model.xml',
        'views/view_property_type.xml',
        'views/view_property_offer_view.xml',
        'views/res_users_view.xml',
        'reports/estate_property_templates.xml',
        'reports/estate_property_report.xml',
       
        
        ],
    'demo' : [
        'demo/real_estate_demo_data.xml',
    ],
    'application' : True,
    'installable' : True,
    'license' : 'LGPL-3',
    'auto_install' : True,
}



