# -*- coding: utf-8 -*-

{
    'name': 'Real Estate',
    'description': 'The Real Estate Advertisement module',
    'version': '1.0',
    'sequence': 1,
    'category': 'Marketing',
    'author': 'Dhrutik Patel (dhrp)',
    'website': 'https://www.odoo.com/',
    'summary': 'The Real Estate Advertisement module',
    'depends': ['mail', 'website'],
    'demo': [
        'demo/estate_property_tag_demo.xml',
        'demo/estate_property_type_demo.xml',
        'demo/estate_property_demo.xml',
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/estate_sold_property_views.xml',
        'views/estate_property_offer.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',
        'views/estate_property_views.xml',
        'views/res_users_inherited_views.xml',
        'views/estate_menus.xml',
        'wizard/estate_property_list_view_inherited.xml',
        'wizard/estate_property_offers_wizard.xml',
        'controllers/estate_property_controller_template.xml',
        'controllers/estate_website_controller_template.xml',
        'report/estate_property_offer_templates.xml',
        'report/estate_user_property_templates.xml',
        'report/estate_reports.xml'
    ],
    'assets': {
        'web.assets_frontend': [
            '/real_estate/static/src/js/description_btn_toggle.js',
        ],
    },
    'category': 'Real Estate/Brokerage',
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
