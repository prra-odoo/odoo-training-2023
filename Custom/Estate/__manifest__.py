{
    'name':'real estate',
    'depends':[
        'base',
        ],
    'license':'LGPL-3',
    'application':True,
    'installable':True,
    'demo':[
        'demo/real_estate_demo_data.xml',
    ],
    'data':[
        'security/ir.model.access.csv',
        'views/estate_property_offer.xml',
        'views/estate_property_tag.xml',
        'views/estate_Type.xml',
        'views/estate_property_views.xml',
        'report/estate_report.xml',
        'report/estate_template.xml',
        'report/res_user_template.xml',
        'views/estate_menus.xml',
    ]
}

