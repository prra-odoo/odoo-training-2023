{
    'name': 'Real Estate',
    'website': 'https://www.odoo.com/page/realestate',
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False,
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_offer_views.xml',
        'views/estate_property_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',
        'views/test_two_views.xml',
        'views/estate_menus.xml',
        'views/users_views.xml',
    ],
    # 'demo': [
    #     'demo/estate_demo.xml'
    # ]
}
