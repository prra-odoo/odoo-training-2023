# -*- coding: utf-8 -*-

{
    'name' : 'RealEstate',
    'category' : 'Sales',
    'summary' : 'Selling Your property',
    'description' : 'This app will help you to find the best deal for your properties',
    'version' : '1.0',
    'author' : 'THSH',
    'data' : [    
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_menus.xml'
        ],
    'demo' : [     ],
    'depends' : [   
      ],
    'installable' : True,
    'application' : True,
    'auto_install' : False
}