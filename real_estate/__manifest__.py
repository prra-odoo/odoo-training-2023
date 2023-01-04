{
    'name': 'REAL ESTATE',
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
        'views/estate_property_tree_view.xml',
        'views/estate_property_form_view.xml',
        'views/estate_property_views.xml',
        'views/estate_menu.xml',
        'security/ir.model.access.csv',

    ],        
    
    'auto_install': False    
}
