# -*- coding: utf-8 -*-

{
    'name' : 'Real Estate',
    'author' : 'Dhrumil Shah',
    'depends' : ['base'],
    'version' : '1.0',
    'data': [
        # 'data/estate.xml',
        'security/ir.model.access.csv',
        'views/view_estate_model.xml',
        'views/action_estate_model.xml',
        'views/view_property_type.xml',
        'views/view_property_offer_view.xml',
       
        
        ],
    'demo' : [
        'demo/real_estate_demo_data.xml',
    ],
    'application' : True,
}
