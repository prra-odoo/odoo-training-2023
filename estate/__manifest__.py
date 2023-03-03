{
    'name': "Real Estate",
    'author': "Shubham Thanki (shut)",
    'sequence': -100,
    'depends': ['base', 'mail'],
    'application': True,
    'license': 'LGPL-3',
    'data': ['security/ir.model.access.csv',
             'views/estate_property_offer_views.xml',
             'views/estate_property_tag_views.xml',
             'views/estate_property_type_views.xml',
             'views/estate_property_views.xml',
             'views/estate_menus.xml',
             'views/res_users_views.xml',
              'report/estate_property_reports.xml',
              'report/estate_property_templates.xml',
               'report/estate_property_offer_templates.xml',
             #    'report/res_users_templates.xml',
             ],
    'demo': [
        'demo/demo_data.xml',
    ]
}
