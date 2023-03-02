{
    'name': 'estate',
    'application': True,
    'license': 'LGPL-3',
    'depends' : ['mail'],
    'data': 
    [
        'data/ir.model.access.csv',
        'views/estate_property_tag.xml',
        'views/estate_property_offer_views.xml',
        'views/estate_property_views.xml',
        'views/estate_property_types.xml',
        'views/estate_menus.xml',
        'views/res_users.xml'
    ],
    'demo' : 
    [
        'demo/estate_property_demo.xml',
        'demo/estate_property_tag_demo.xml',
        'demo/estate_property_types_demo.xml',
    ]
}