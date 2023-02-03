{
    'name': "Real Estate",
    'version': '1.0',
    'depends': ['base','mail','website',],
    'author': "Gurpreet Singh(gusi)",
    'category': 'real_estate/Brokerage',
    'description': "This is a Real Esate App",
    'summary': "This is a Real Esate App developed in odoo(OWL Framework)",
    'installable': True,
    'application': True,
    'data': [
        
        'security/security.xml',
        'security/ir.model.access.csv',
        'report/report_property_users_template.xml',
        'report/real_estate_property_reports.xml',
        'report/real_estate_templates.xml',
        'report/Inherit_real_estate_report.xml',
        'views/website_menu.xml',
        'views/real_estate_template.xml',
        'views/real_estate_menu.xml',
        'views/real_estate_property_views.xml',
        'views/real_estate_property_tags_view.xml',
        'views/real_estate_property_type_view.xml',
        'views/real_estate_porperty_offer_view.xml',
        'views/res_users_views.xml',
    ],
    'demo': [
        'demo/estate_demo.xml',
        'demo/real_estate_property_type_data.xml',
        'demo/real_estate_property_data.xml',
        'demo/real_estate_property_tags_data.xml',
        #  'demo/real_estate_property_offer_data.xml',
    ],
    'assets':{
        'web.assets_frontend':[
            'real_estate/static/css/main.scss'
        ]},
}
