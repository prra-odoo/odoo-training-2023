{
    'name' : 'Estate',
    'installable': True,
    'application': True,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        
        'views/res_users_views.xml',
        'views/estate_property_views.xml',
        'views/estate_property_offer_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',
        'views/estate_menus.xml',
        'report/estate_property_templates.xml',
        'report/estate_property_reports.xml'
    ],
    'demo' : [
        'data/estate_property_data.xml',
    ],
    'license' : 'LGPL-3',
    'auto_install': True
}