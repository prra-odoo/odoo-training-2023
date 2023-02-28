{
    'name': "Real Estate",
    'author': "Shubham Thanki (shut)",
    'sequence': -100,
    'depends': ['base'],
    'application': True,
    'license': 'LGPL-3',
    'data': ['security/ir.model.access.csv',
             'views/estate_property_offer_views.xml',
             'views/estate_property_tag_views.xml',
             'views/estate_property_type_views.xml',
             'views/estate_property_views.xml',
             'views/estate_menus.xml',
             'views/res_users_views.xml'
             ],
    'demo': [
        'demo/demo_data.xml',
    ]
}
