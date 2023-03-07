# -*- coding: utf-8 -*-
{
    'name':"Real Estate",
    'depends':['base','mail','website'],
    'license':"LGPL-3",
    'category':"Real Estate/Brokerage",
    'data':[
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/estate_property_offer_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',
        'views/estate_property_views.xml',
        'views/estate_menus.xml',
        'views/res_users_views.xml',
        'views/templates.xml',
        'report/estate_property_templates.xml',
        'report/estate_property_reports.xml',
        'data/master_data.xml',],

    'demo':[
        'data/demo_data.xml',
    ],
    'application': True
}
