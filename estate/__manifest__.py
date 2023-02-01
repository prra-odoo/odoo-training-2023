# -*- coding: utf-8 -*-
{
    'name' : 'Real Estate',
    'category': 'Real Estate/Brokerage',
    'description' : """this is the real estate advertisement module""",
    'depends': ['mail','website', 'website_sale'],
    'data' : [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/estate_property_menu.xml',
        'views/estate_property_view.xml',
        'views/estate_property_type_view.xml', 
        'views/estate_property_tag_view.xml',
        'views/estate_property_offer_view.xml',
        'views/templates.xml',
        'views/res_users_view.xml',
        'report/estate_property_templates.xml',
        'report/estate_property_reports.xml',
    ],
    'demo' : [
        'demo/estate_property_type_demo_data.xml',
        'demo/estate_tag_demo_data.xml',
        'demo/estate_demo_data.xml',
    ],
    'application' : True,
}
