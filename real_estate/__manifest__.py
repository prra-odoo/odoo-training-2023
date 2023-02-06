{
    'name': 'Real Estate',
    'version': '1.0',
    'category': 'Real Estate/Brokerage',
    'depends':[
        'mail',
        'calendar',
        'contacts',
        'website'
       ],
    'author': 'Archana',
    'summary': 'Track estate properties',
    'description': 'Real estate module',
    'installable': True,
    'application': True,
    'data':[
         'security/real_estate_security.xml', 
         'security/ir.model.access.csv',
         'data/estate_property_type_data.xml',
         'data/estate_property_tag_data.xml',
        #  'data/website_menu.xml',
         'views/estate_property_actions.xml',
         'views/estate_property_menu.xml',
         'views/estate_property_views.xml',
         'wizard/estate_property_offer_wizard_view.xml',
         'data/estate_property_data.xml',
         'views/estate_property_type_view.xml',
         'views/estate_property_tags_view.xml',
         'views/estate_property_offer_view.xml',
         'views/res_users_view.xml',
         'views/user_data_view.xml',
         'views/search.xml',
         'views/template.xml',
    
         'report/estate_template.xml',
         'report/estate_property_report.xml',
        #  'data/user_data.xml',
    ]
}