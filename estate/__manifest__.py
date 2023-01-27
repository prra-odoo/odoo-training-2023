# -*- coding: utf-8 -*-

{
    'name' : 'Estate Property',
    'description' : 'Advertisment Module of Real Estate',
    'category' : 'Real_Estate/Brokerage',
    'data' :[
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/estate_views_actions.xml',
        'views/estate_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',
        'views/estate_property_offer_views.xml',
        'views/res_users_model_views.xml',
    ],
    # 'demo' :[
    #     'demo/estate_demo_data.xml',
    #     ],
    'depends' : ['base','mail','portal'],
    'application' : True
}