{
    'name': 'estate',
    'application': True,
    'license': 'LGPL-3',
    'depends' : ['mail'],
    'data': 
    [
        'data/security.xml',
        'data/ir.model.access.csv',
        'views/estate_property_offer_views.xml',
        'views/estate_property_tag.xml',
        'views/estate_property_types.xml',
        'views/estate_property_views.xml',
        'views/estate_menus.xml',
        'views/templates.xml',
        'report/estate_property_templates.xml',
        'report/estate_property_reports.xml',
        'views/res_users.xml',
    ],
    'demo' : 
    [
        'demo/demo_data.xml'
    ],
    'category': 'estate/brokerage',
}