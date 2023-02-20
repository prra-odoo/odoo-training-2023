# -- coding: utf-8 --

{
'name': 'Estate',
    'version': '1',
    'sequence': 1,
    'summary': 'Real estate around',
    'description': "--demo description--",
    'category': 'Real Estate/Brokerage',

    'data': [
        'security/estate_security.xml',
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_menus.xml',
        'views/estate_property_offer_views.xml',
        'views/res_user_view.xml',
        'views/settings_menu.xml',
        'controllers/property_template.xml',
        'reports/estate_property_reports.xml',
        'reports/estate_property_templates.xml'
    ],

    'demo':[
        'demo/demo_properties.xml'
    ],

    'depends' : ['mail','website'],
    
    'installable': True,
    'application': True,
}    