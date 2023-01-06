{
    'name': "Real_estate",
    'version': '1.0',
    'depends': ['base'],
    'author': "Tejas Modi(temo)",
    'category': 'Sales',
    'description': "This is real estate module",
    'summary':'hello',
    'installable':'true',
    'application':'true',
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_action.xml',
        
    ],
     'demo':[
        'demo/estate_demo.xml',
        'demo/estate_propertytype_demo.xml',
     ]
}
