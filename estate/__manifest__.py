# -*- coding: utf-8 -*-
{
    "name":"Real Estate",
    "version":"1.0",
    "author":"Aditya Sharma",
    "category":"Real Estate/Brokerage",
    "description": 'Real estate Advertising module',
    "depends": ['mail','base','website','website_sale'],
    "data": [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_action.xml',  
        
        'reports/reports.xml',
        'reports/templates.xml',
        'reports/template_web.xml',

        'wizard/estate_property_put_offer.xml'
    ],
    'demo':[
        'demo/demo_data.xml',
    ],

    "application": True,
}