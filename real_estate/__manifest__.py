# -- coding: utf-8 --

{
    'name':'real_estate',
    'data': [
        'security/ir.model.access.csv',
        'views/estate_menu_view.xml',
        'views/estate_menu.xml',
        'views/estate_type_view.xml',
        
    ],
    'depends': ['mail','base'],
    'demo': [
        'demo/estate_demo_data.xml',
    ],
    'application':True,
    'installable':True,
}