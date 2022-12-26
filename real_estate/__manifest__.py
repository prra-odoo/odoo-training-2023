# -*- coding:utf:8 -*-

{
    'name' : "Real Estate",
    'author' : "Sanket Brahmbhatt(sabr)",
    'summary' : "Creating Real Estate Model",
    'version' : '1.0' ,
    'data' : [
            #   'data/estate_demodata.xml',
              'views/estate_property_views.xml',
              'views/estate_property_menus.xml',
              'security/ir.model.access.csv',
    ],
    'application' : True,
    'installable': True,
    'license': 'LGPL-3',
    'demo': [
        'demo/estate_property_demo_data.xml',
    ],
}