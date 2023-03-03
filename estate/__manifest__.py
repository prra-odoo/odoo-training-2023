# -- coding: utf-8 -
{
    'name': "Real Estate",
    'depends': ['base', 'mail',  'portal'],
    'application': True,
    'license' : 'LGPL-3',
    'data' : ['security/ir.model.access.csv',
              'report/estate_property_reports.xml',
              'report/estate_property_templates.xml',
              'views/estate_property_views.xml',
              'views/estate_property_tag_views.xml',
              'views/estate_property_offer_views.xml',
              'views/estate_property_types_views.xml',
              'views/res_users_views.xml',
              'views/estate_property_menus.xml',
              'data/estate_property_master_data.xml'
              
             ],
    'demo': [
        "demo/estate_property_demo.xml"
            ]
}   