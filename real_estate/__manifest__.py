# -*- coding: utf-8 -*-

{
    'name': 'Real Estate',
    'description': 'The Real Estate Advertisement Module',
    'version': '1.0',
    'author': 'Renilkumar Kajavadra',
    'depends':['base','mail','account','website'],
    'category': 'Real Estate/Brokerage',
    'data': [
                'security/security.xml',
                'security/ir.model.access.csv',
                'views/estate_property_menus.xml',
                'views/estate_property_views.xml',
                'views/estate_property_offer_view.xml',
                'views/estate_property_type_view.xml',
                'views/estate_property_tags_view.xml',
                'views/res_users_view.xml',
                'views/estate_property_controller.xml',
                'reports/estate_property_templates.xml',
                'reports/estate_property_reports.xml',
                'wizard/estate_property_wizard.xml'
            ],
    'demo': [
                'demo/demo.xml'
            ],
    'application' : True,
    'installable': True,
    'license': 'LGPL-3'
}
