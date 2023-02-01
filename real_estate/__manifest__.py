# -*- coding: utf-8 -*-

{
    'name': "Real Estate",
    'version': '1.0',
    'depends': ['base', 'mail', 'website'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/estate_property_offers_views.xml',
        'report/estate_property_reports.xml',
        'report/estate_property_templates.xml',
        'views/estate_property_views.xml',
        'views/estate_tag_views.xml',
        'views/estate_type_views.xml',
        'views/inherited_res_user_model_views.xml',
        'views/estate_property_menus.xml',
        'report/templates.xml',
        'demo/estate_property_demo_data.xml',
        'demo/estate_type_demo_data.xml',
        'demo/estate_tag_demo_data.xml',
        'demo/estate_offers_demo_data.xml',
        'demo/estate_category_demo_data.xml',
    ],

    'author': "rare",
    'category': 'Real Estate/Brokerage',    
    'description': """
        This is my Real Estate Module.
        Created by rare!
    """,
    'installable': True,
    'application': True,
}