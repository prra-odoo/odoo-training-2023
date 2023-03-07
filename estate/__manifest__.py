{
    'name':'Real estate',
    'depends' : ['mail'],
    'summary':'This is a real estate module',
    'author':'Arjun Panchal',
    'version':'1.0',
    'installable': True ,
    'application': True,
    'auto_install': True,
    'license': 'LGPL-3',
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/estate_property_view.xml',
        'views/estate_property_tag_view.xml',
        'views/estate_property_offer_view.xml',
        'views/estate_property_type_view.xml',
        'views/estate_menu.xml',
        'views/res_users_views.xml',
        'report/estate_property_templates.xml',
        'report/estate_property_reports.xml',
        'views/templates.xml',
        ],

    'demo':[
    'demo/estate_demo.xml'
    ],  
    'category': 'estate/Brokerage',
}