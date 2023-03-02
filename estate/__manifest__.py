{
    'name' : 'Estate',
    'installable': True,
    'application': True,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        
        'data/estate_property_type_data.xml',
        'data/estate_property_data.xml',

        'views/res_users_views.xml',
        'views/estate_property_views.xml',
        'views/estate_property_offer_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',
        'views/estate_menus.xml',
    ],
    'license' : 'LGPL-3',
    'auto_install': True
}