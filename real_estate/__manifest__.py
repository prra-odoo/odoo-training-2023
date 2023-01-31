# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Real Estate',
    'version': '1.0',
    'depends': ['base'],
    'author': 'mobe',
    'category' :'Real Estate/Brokerage',
    'data' : [
         'security/security.xml',
         'security/ir.model.access.csv',
         'views/estate_property_menus.xml',
         'views/estate_property_views.xml',
         'views/property_type_views.xml',
         'views/property_tags_views.xml',
         'views/property_offer_views.xml',
         'views/res_users_views.xml',
         'report/estate_property_templates.xml',
         'report/estate_property_reports.xml',
         'report/estate_user_reports.xml',

    ],
    'demo' : [
        'demo/estate_properties_demo.xml',
        'demo/estate_property_type_demo.xml',
        'demo/estate_property_tag_demo.xml',

    ],
    'application' : True,
    'installable' :True,
    'auto_install' : False,
    "license": "LGPL-3",
}