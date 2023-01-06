{
    'name': "Real Estate",
    'version': '1.0',
    'depends': ['base'],
    'author': "Gurpreet Singh(gusi)",
    'category': 'Sales',
    'description': "This is a Real Esate App",
    'summary': "This is a Real Esate App developed in odoo(OWL Framework)",
    'installable': True,
    'application': True,
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/real_estate_property_type_view.xml',
        'views/real_estate_menu.xml',
    ],
    'demo': [
        'demo/real_estate_property_type_data.xml',
        'demo/estate_property_data.xml',
    ],
}
