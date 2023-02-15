# -*- coding: utf-8 -*-
{
    'name': "Real Estate",
    'summary': "Module for real estate",
    'author': "Ayushi Gorai(aygo)",
    'category': 'Real Estate/Brokerage',
    'license': 'LGPL-3',
    'description': "real estate module",        
    'installable':True,
    'application':True,
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'view/estate_property_offer_view.xml',
        'view/estate_property_views.xml',
        'view/res_users_view.xml',
        'view/estate_property_type_view.xml',
        'view/estate_property_tag_view.xml',
        'view/estate_menus.xml',
      ],
    'demo': [
      'demo/real_estate_tag_data.xml',
      'demo/real_estate_type_data.xml',
      'demo/real_estate_demo_data.xml',
     ],
     'depends' : ['mail'],
     'icon' : "estate/static/description/real-estate.png",
}