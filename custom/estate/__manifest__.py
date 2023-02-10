# -- coding: utf-8 -
{
    'name': "Real Estate",
    'depends': ['base'],
    'application': True,
    'data':[
        'security/ir.model.access.csv',
        
        'views/estate_property_views.xml',
        'views/estate_property_tags.xml',
        'views/estate_property_types.xml',
        'views/estate_menus.xml'
        
    ],
    'license':'LGPL-3'

    
}