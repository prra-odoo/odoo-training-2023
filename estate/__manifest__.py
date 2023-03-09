{
    'name': "Real Estate",
    'version': '1.0',
    'depends': ['base','mail','website'],
    'author': "Author Name",
    'category': 'Category',
    'license': 'LGPL-3',
    
    'description': """
    Description text
    """,
        
    'data': [
        'security/ir.model.access.csv',
        'report/estate_property_website_templates.xml',
        'report/estate_property_templates.xml',
        'report/estate_property_reports.xml',
        'report/res_user_template.xml',
        'views/estate_property_views.xml',
        'views/estate_property_offer_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_tags_views.xml',        
        'views/estate_menus.xml'

    

    ],

    'demo': [
        'demo/demo_data.xml',
    
    ],

    'application': True,
    'installable': True,

}
