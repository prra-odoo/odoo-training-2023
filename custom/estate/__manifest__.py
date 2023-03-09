{
    'name': 'Real Estate',
    'website': 'https://www.odoo.com/page/realestate',
    'license': 'LGPL-3',
    'category': 'Real Estate/Brokerage',
    'installable': True,
    'application': True,
    'auto_install': False,
    'depends' : ['base','mail','website'],
    'data': [
        'security/estate_security.xml',
        'security/ir.model.access.csv',
        'report/estate_property_reports.xml',
        'report/estate_property_templates.xml',
        'views/estate_property_offer_views.xml',
        'views/estate_property_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',
        'views/estate_menus.xml',
        'views/users_views.xml',
        'controllers/estate_website_template.xml'
    ],
    'demo': [
        'demo/estate_demo.xml',
    ]
}
