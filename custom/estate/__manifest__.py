
{
    'name': "estate"   , 
    'depends':['base','mail','website'], 
    'application': True,
    'version': '1.0',
    'license': 'LGPL-3',    
    'category':'Real Estate/Brokerage',
    'data':[
            'security/security.xml',
            'security/ir.model.access.csv',
            'report/estate_property_reports.xml',
            'report/estate_property_templates.xml',
            'views/estate_property_offer_view.xml',
            'views/estate_property_tag_views.xml',
            'views/estate_property_types_views.xml',
            'views/estate_property_views.xml',
            'views/estate_menus.xml',
            'controller/templates.xml',
            'wizard/estate_create_offer_view.xml'
    ],
    'demo':[ 'demo/estate_demo_data.xml',],
    'images':['static/description/icon.png'],
}

