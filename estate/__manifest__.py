{
    'name':'estate',
    
    'depends' : ['mail'],
 
    'data':[
        'security/ir.model.access.csv',
        'views/estate_property_offer_view.xml',
        'views/estate_property_view.xml',
        'views/estate_property_type_view.xml',
        'views/estate_property_tags_view.xml',
        'views/res_users_view.xml',
        'views/estate_menus.xml',
        'reports/estate_property_templates.xml',
        'reports/estate_property_offer_templates.xml',
        'reports/estate_property_reports.xml', 
    ],
    
    'demo':[
        'demo/demo_data.xml',  
    ],
    
    
    
    'installable':True,
    'application':True,
    'license':'LGPL-3', 
}