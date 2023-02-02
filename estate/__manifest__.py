# -*- coding: utf-8 -*-

{
    'name' : "Real Estate",
    'version' : '1.0',
    'author' : "Saurabh Choraria",
    'description' : "It is a module for real estate",
    'depends' : ['mail', 'base', 'website', 'event', 'website_sale'],
    'category' : 'Real Estate/Brokerage',
    'data' : [
            'security/estate_security.xml',
            'security/ir.model.access.csv',
            
            'views/estate_property_offer_views.xml',
            'views/estate_property_tags_views.xml',
            'views/estate_property_type_views.xml',
            'views/estate_property_views.xml',
            'views/inherited_model_views.xml',
            'views/estate_views_action.xml',

            'report/estate_property_templates.xml',
            'report/estate_account_templates.xml',
            'report/estate_property_reports.xml',
            'report/controller_templates.xml'
        ],
    'demo' : [
            'demo/estate_demo.xml',
        ],    
    'application' : True,
}
