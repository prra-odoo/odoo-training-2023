
{
    'name': "Real Estate",
    'application': True,
    'sequance':1,
    'version': '1.0',
    'depends': ['base'],
    'author': "ZEPA",
    'category': 'Category',
    'summary': """
    Real Estate module Training
    """,
    'installable': True,
    'license': 'LGPL-3',

    'data' : [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_menu.xml'
    ]
    

}