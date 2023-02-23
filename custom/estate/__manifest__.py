
{
    'name': "estate"   , 
    'depends':['base',], 
    'application': True,
    'license': 'LGPL-3',    
    'data':['security/ir.model.access.csv',
            'views/estate_property_offer_view.xml',
            'views/estate_property_tag_views.xml',
            'views/estate_property_types_views.xml',
            'views/estate_property_views.xml',
            'views/estate_menus.xml',
    ],
    'demo':[ 'demo/estate_demo_data.xml',],

}

