# -*- coding: utf-8 -*-
{
    'name' : 'Real Estate',
    'version' : '1.0',
    'summary' : 'Manage Real Estate Properties',
    'depends' : ['base'],
    'data' : [
        'security/ir.model.access.csv',
        'views/estate_menus.xml',
        'views/estate_property_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_offer_views.xml'
    ],
    'demo': [
        'demo/estate_property_demo.xml',
        'demo/estate_property_tags_demo.xml',
        'demo/estate_property_type_demo.xml',
    ],
    'installable' : True,
    'application' : True,
}
