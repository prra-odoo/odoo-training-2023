{
    'name': 'REAL_ESTATE',
    'version': '2.0',
    'description': 'Real Estate Module',
    'author': 'odoo',
    'category': 'marketing',
    'installable': True, 
    'summary': 'real estate advertisement', 
    'application': True,
    
    'depends': [
    ],

    'data': [
        'views/estate_property_views.xml',
        'security/ir.model.access.csv',

    ],        
    
    'auto_install': False    
}
