# -*- coding: utf-8 -*-
{
    'name' : 'real estate',
    'description' : " Real estate module",
    'version' :'',
    'author':'Althaf Shaik',
    'category':'Real Estate/Brokerage',
    'depends':['mail', 'base'],
    'data':[
         'security/ir.model.access.csv',
         'security/security.xml',
         'views/estate_properties_menus.xml',
         'views/estate_properties_view.xml',
         'views/estate_property_type_view.xml',
         'views/estate_properties_offer_view.xml', 
         'views/res_user_view.xml',
        ],
    'demo':[
        'demo/demo_data.xml',
        'demo/real_estate_tag_demo.xml',
        'demo/real_estate_type_demo.xml',

        ],
    'application' : True,
    
}