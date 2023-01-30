{
    'name': 'real_estate',
    'version': '1.0',
    'category': 'Real Estate/Brokerage',
    'summary': 'Find rates of real estates',
    'description': "App for Real Estate management",
    'author': 'sami',
    'license': 'LGPL-3',
    'depends':['base','mail'],
    'data': [
        'security/real_estate_security.xml',
        'security/ir.model.access.csv',
        'views/real_estate_menu.xml',
        'views/estate_property_views.xml',
        'views/estate_property_offer.xml',
        'views/estate_property_type.xml',
        'views/estate_property_tag.xml',
        'views/res_user_prac.xml',
        'report/estate_property_templates.xml',
        'report/estate_property_reports.xml',
       
  
        
    ],
    'demo': [
        'demo/estate_property_tag_demo.xml',
        'demo/estate_property_demo.xml',
        'demo/estate_property_type_demo.xml',
        # 'demo/estate_property_offer_demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False

}



