{
    'name': "Real Estate",
    'depends':['base'],
    'version': '1.0.0',
    'sequence': -100,
    'author': 'sankalp (schh)',
    'category': 'Management',
    'installable': True,
    'application':True,
    'license': 'LGPL-3',
    'summary': 'Application to manage your real estate business',
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_purchase_views.xml',
        'views/estate_menus.xml'
    ]
}
