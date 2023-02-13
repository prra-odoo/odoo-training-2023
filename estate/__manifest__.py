# -- coding: utf-8 --

{
'name': 'Estate',
    'version': '1',
    'sequence': 1,
    'summary': 'Real estate around',
    'description': "--demo description--",
    'category': 'Real Estate/Brokerage',

    'data': [
        'security/ir.model.access.csv',
        'security/estate_security.xml',
        'views/estate_property_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_menus.xml',
        'views/estate_property_offer_views.xml',
        'views/res_user_view.xml',
        'views/settings_menu.xml',
    ],

    'demo':[
        'demo/demo_properties.xml'
    ],

    'depends' : ['mail'],
    
    'installable': True,
    'application': True,
}    