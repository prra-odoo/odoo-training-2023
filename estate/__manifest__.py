{
    'name':"Real Estate",
    'depends': ['base','mail','website','website_blog','website_event'],
    'application': True,
    'license' : 'LGPL-3',
    'data' : [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/res_users_views.xml',
        'views/estate_property_offer_views.xml',
        'views/estate_property_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',
        'reports/estate_property_reports.xml',
        'reports/estate_property_templates.xml',
        'controllers/controller_property_templates.xml',
        'views/estate_menus.xml',
        'wizards/wizard_views.xml'],
    'demo' : [
        'demo/estate_property_demo_data.xml'
    ],
    'category': 'Real Estate/Brokerage'
}