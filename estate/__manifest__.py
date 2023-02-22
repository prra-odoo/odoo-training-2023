{
    'name':"Real Estate",
    'depends': ['base'],
    'application': True,
    'license' : 'LGPL-3',
    'data' : [
        'views/estate_property_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',
        'views/estate_property_offer_views.xml',
        'views/estate_menus.xml',
        'security/ir.model.access.csv',],
    'demo' : [
        'demo/estate_property_demo_data.xml'
    ]
}