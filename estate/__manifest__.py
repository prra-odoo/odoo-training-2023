# -*- coding: utf-8 -*-
{
    'name' : 'real estate',
    'description' : " Real estate module",
    'version' :'',
    'author':'Althaf Shaik',
    'category':'Advertising',
    'depends':['mail',],
    'data':[
         'security/ir.model.access.csv',
         'views/estate_properties_view.xml',
         'views/estate_properties_menus.xml',
         'views/estate_properties_offer_view.xml',
         'views/estate_property_type_view.xml',
        ],
    'demo':[
        'demo/demo_data.xml',
        ],
    'application' : True,
    
}