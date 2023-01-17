# -*- coding:utf:8 -*-
{
    'name': "Real Estate",
    'author': "Sanket Brahmbhatt(sabr)",
    'summary': "Creating Real Estate Model",
    'version': '1.0',
    'depends': ['mail'],
    'data': [
        #   'data/estate_demodata.xml',
        'views/estate_property_offer_view.xml',
        'views/estate_property_type_view.xml',
        'views/estate_property_tag_views.xml', 
        'views/estate_property_views.xml',
        'views/res_user_view.xml',
        'views/estate_property_menus.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [
        'demo/estate_property_demo_data.xml',
        'demo/estate_property_type_demo.xml',
        'demo/estate_property_tag_demo_data.xml',
    ],
    'application': True,
    'installable': True,
    'license': 'LGPL-3',

}
