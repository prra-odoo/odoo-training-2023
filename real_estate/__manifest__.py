{
    'name': 'Real Estate',
    'version': '1.0',
    'category': 'Marketing',
    'depends':[
        'calendar',
        'contacts',
       ],
    'author': 'Archana',
    'summary': 'Track estate properties',
    'description': 'Real estate module',
    'installable': True,
    'application': True,
    'data':[
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
    ]
}