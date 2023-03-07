{
    'name': 'Real Estate',
    'application':True,
    'version': '1.0',
    'depends': ['base','mail','website'],
    'author': 'PRPA',
    'category': 'Category',
    'summary': 'Real Estate Module Training',
    'license': 'LGPL-3',
    'installable': True,
    'data' : [
        'security/ir.model.access.csv',
        'controller/templates.xml',
        'views/res_user.xml',
        'report/estate_property_reports.xml',
        'report/estate_property_templates.xml',
        'views/estate_property_views.xml',
        'views/estate_property_offer_view.xml',
        'views/estate_property_type_view.xml',
        'views/estate_property_tag_view.xml',
        'views/estate_menus.xml'
    ],
     
    'demo' : [
        'demo/estate_property_demo.xml',
    ]   
    
}