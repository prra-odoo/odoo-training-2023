# -*- coding: utf-8 -*-
{
    'name' : 'Real_Estate',
    'author': "Ravi Bhingradiya",
    'depends': ['mail','website','website_sale'],
    'category': 'Real Estate/Brokerage',
    'data' : [
            'security/security.xml',
            'security/ir.model.access.csv',
            'views/estate_menus.xml',
            'views/estate_property_view.xml',
            'views/estate_property_type_view.xml',
            'views/estate_property_offer_view.xml',
            'views/res_users_view.xml',
            'report/estate_property_templates.xml',
            'report/estate_property_reports.xml',
    ],

    'demo' : [ 
            'data/real_estate_demo_data.xml',
            'data/website_demo_data.xml',
    ],

    'application' : True,
    'installable': True,
    'license': 'LGPL-3',
}