# -- coding: utf-8 --

{
    'name':'real_estate',
    'category': 'Real Estate/Brokerage',
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/estate_menu_view.xml',
        'views/estate_menu.xml',
        'views/estate_type_view.xml',
        'views/estate_offer_view.xml',
        'views/res_user_view.xml',
        'report/estate_property_report.xml',
        'report/estate_property_templates.xml',
        
    ],
    'depends': ['mail','base'],
    'demo': [
        'demo/estate_demo_data.xml',
    ],
    'application':True,
    'installable':True,
}