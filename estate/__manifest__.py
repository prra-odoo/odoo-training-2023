# -- coding: utf-8 --

{
'name': 'Estate',
    'version': '1',
    'sequence': 1,
    'summary': 'Real estate around',
    'description': "--demo description--",

    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_menus.xml',
        'views/settings_menu.xml',
        'views/estate_property_offer_views.xml',
    ],
    'installable': True,
    'application': True,
}    