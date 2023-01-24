# -*- coding: utf-8 -*-
{
    'name': "Real Estate",
    'summary': "Module for real estate",
    'author': "Ayushi Gorai(aygo)",
    'category': 'Category',
    'license': 'LGPL-3',
    'description': "real estate module",
    'installable':True,
    'application':True,
    'demo': [
      'demo/real_estate_demo_data.xml',
     ],
     'data': [
        'security/ir.model.access.csv',
        'view/estate_property_views.xml',
        'view/estate_property_type_view.xml',
        'view/estate_property_tag_view.xml',
        'view/estate_property_offer_view.xml',
        'view/estate_menus.xml',
     ],
     'depends' : ['mail'],
}