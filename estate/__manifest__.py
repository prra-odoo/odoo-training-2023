# -*- coding: utf-8 -*-
{
    'name' : 'Real Estate',
    'description' : """"this is the real estate advertisement module""",
    'depends': ['mail'],
    'data' : [
        'security/ir.model.access.csv',
        'views/estate_property_menu.xml',
        'views/estate_property_view.xml',
        'views/estate_property_type_view.xml', 
        'views/estate_property_tag_view.xml',
        'views/estate_property_offer_view.xml',
        'views/res_users_view.xml',
    ],
    'demo' : [
        'demo/estate_demo_data.xml',
    ],
    'application' : True,
}