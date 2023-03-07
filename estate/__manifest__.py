
{
    'name': "Real Estate",
    'application': True,
    'sequence':1,
    'version': '1.0',
    'depends': ['base','mail','website'],
    'author': "ZEPA",
    'category': 'Category',
    'summary': """
    Real Estate module Training
    """,
    'installable': True,
    'license': 'LGPL-3',

    'data' : [
        'security/ir.model.access.csv',
        'report/templates.xml',
        'report/estate_property_template.xml',
        'report/property_res_user_template.xml',
        'report/estate_property_report.xml',
        'views/res_user_view.xml',
        'views/estate_property_offer_view.xml',
        'views/estate_property_views.xml',
        'views/estate_property_type_view.xml',
        'views/estate_property_tag_view.xml',
        'views/estate_menu.xml',
    ],
    'demo' : [ 
        'demo/estate_property_type_data.xml',
        'demo/estate_property_tag_data.xml',
        'demo/estate_property_data.xml',
    ],
    
}