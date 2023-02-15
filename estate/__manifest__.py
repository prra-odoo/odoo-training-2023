{
    'name':'Real estate',
    'depends':['base'],
    'summary':'This is a real estate module',
    'author':'Arjun Panchal',
    'version':'1.0',
    'installable': True ,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_view.xml',
        'views/estate_property_tag_view.xml',
        'views/estate_property_type_view.xml',
        'views/estate_property_offer_view.xml',
        'views/estate_menu.xml',
        ]
}