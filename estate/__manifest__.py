{
    'name' : 'estate',
    'installable': True,
    'application': True,
    'depends': ['sale_management'],
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_menus.xml',
    ],
    'license' : 'LGPL-3',
}