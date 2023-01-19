# -*- coding: utf-8 -*-

{
    'name': 'Real Estate',
    'description': 'The Real Estate Advertisement Module',
    'author': 'Renilkumar Kajavadra',
    'depends':['base','mail'],
    'data': [
                'security/ir.model.access.csv',
                'views/estate_property_menus.xml',
                'views/estate_property_views.xml',
                'views/estate_property_offer_view.xml',
                'views/estate_property_type_view.xml',
                'views/estate_property_tags_view.xml',
                'views/res_users_view.xml'
            ],
    'demo': [
                'demo/demo.xml'
            ],
    'application' : True,
    'installable': True,
    'license': 'LGPL-3'
}
