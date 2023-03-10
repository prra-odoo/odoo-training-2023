#--coding: utf-8 -
{
    'name': "Aman Real Estate",
    'depends': ['base', 'mail',  'portal','website'],
    'application': True,
    'license' : 'LGPL-3',
    'data':['security/ir.model.access.csv',
            'security/security.xml',

            'wizard/wizard.xml',


            'report/estate_property_reports.xml',
            'report/estate_property_templates.xml',
            'views/estate_property_offer_views.xml',
            'views/estate_property_views.xml',
            'views/estate_property_type_views.xml',
            'views/estate_property_tag_views.xml',
            'views/res_users_views.xml',
            'data/estate_property_master_data.xml',
            'controller/templates.xml',
            'views/estate_menus.xml'
            ],
    'demo' : ['demo/realestate_demo_data.xml'],
    'category': 'Real Estate/Brokerage'

}