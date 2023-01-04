# -*- coding: utf-8 -*-

{
    'name' : "Real Estate",
    'version' : '1.0',
    'author' : "Saurabh Choraria",
    'description' : "It is a module for real estate",
    'depends' : ['mail'],
    'data' : [
            'views/estate_property_views.xml',
            'views/estate_property_type_views.xml',
            'views/estate_views_action.xml',
            'security/ir.model.access.csv',
        ],
    'demo' : [
            'demo/estate_property_demo.xml',
        ],    
    'application' : True,
}
