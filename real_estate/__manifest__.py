{
    'name': 'Real Estate',
    'application':True,
    'version': '1.0',
    'depends': ['base'],
    'author': 'PRPA',
    'category': 'Category',
    'summary': 'Real Estate Module Training',
    'license': 'LGPL-3',
    'installable': True,
    'data' : [
        'security/ir.model.access.csv',
        'views/res_user.xml',
        'views/estate_property_views.xml',
        'views/estate_property_offer_view.xml',
        'views/estate_property_type_view.xml',
        'views/estate_property_tag_view.xml',
        'views/estate_menus.xml'
    ],
     
    'demo' : [
        'demo/estate_property_demo.xml',
    ]
    
}