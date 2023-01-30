# -*- coding: utf-8 -*-

{
    'name': "Real Estate",
    'version': '1.0',
    'author': "yava",
    'description': "You can easily apply your core project modual with odoo's Real Estate ",
    'depends': ['mail'],
    'data': [
        'security/estate_property_security.xml',
        'security/ir.model.access.csv',
        'data/estate_menus.xml',
        'views/estate_property_views.xml',
        'views/estate_property_menuitem.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',
        'views/estate_property_offer.xml',
        'views/res_users_view.xml',
        'report/estate_property_reports.xml'
    ],
    'demo': [
        'demo/estate_property_tags_demo_data.xml',
        'demo/estate_property_type_demo_data.xml',
        'demo/estate_property_demo_data.xml',
    ],
    'application': True,
    'installable': True,
    'license': "LGPL-3",
    'website': 'https://www.odoo.com',


}
