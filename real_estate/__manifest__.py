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
    'demo':[
          'demo/estate_property_demo.xml',
          'demo/estate_property_tag_demo.xml',
          'demo/estate_property_type_demo.xml',


   ],

    'data': [
        
        'security/ir.model.access.csv',
        'views/estate_property_tag.xml',
        'views/estate_property_type.xml',
        'views/estate_property_sales.xml',
        'views/estate_property_buyer.xml',
        'views/estate_property_offer.xml',
        'views/estate_property_views.xml',
        'views/estate_menu.xml',   

    ],        
    
    'auto_install': False    
}
