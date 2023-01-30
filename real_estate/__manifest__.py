{
    'name': 'Real Estate',
    'version': '2.0',
    'description': 'Real Estate Module',
    'author': 'odoo',
    'category': 'Real Estate/Brokerage',
    'installable': True, 
    'summary': 'real estate advertisement', 
    'application': True,
    
    'depends': [
          'mail',
    ],
    'demo':[
          'demo/estate_property_tag_demo.xml',
          'demo/estate_property_type_demo.xml',
          'demo/estate_property_demo.xml',
          
   ],

    'data': [
        'security/estate_security.xml',
        'security/ir.model.access.csv',
        'views/estate_menu.xml',
        'views/estate_property_tag.xml',
        'views/estate_property_type.xml',
        'views/estate_property_sales.xml',
        'views/estate_property_buyer.xml',
        'views/estate_property_offer.xml',
        'views/estate_property_views.xml',
        'views/inherited_model.xml',
        'report/estate_property_reports.xml',
        'report/estate_property_templates.xml',
           

    ],        
    
    'auto_install': False    
}
