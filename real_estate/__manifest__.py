{
    'name':'Real Estate',
    'version':'0.1',
    'depends':['mail','website'],
    'author':'Harsh Modi (hamo)',
    'category':'Real Estate/Brokerage',
    'data':[
        'security/ir.model.access.csv',
        'security/security.xml',
        'templates/property_template.xml',
        'templates/index_template.xml',
        'data/estate_data.xml',
        'reports/estate_salesman_templates.xml',
        'reports/estate_property_templates.xml',
        'reports/estate_property_reports.xml',
        'views/inherited_model_views.xml',
        'views/inherited_res_partner_views.xml',
        'wizard/offers2property_view.xml',
        'views/real_estate_property_views.xml',
        'views/real_estate_property_offer_views.xml',
        'views/real_estate_property_type_views.xml',
        'views/real_estate_property_tags_views.xml',
        'views/real_estate_menus.xml'
    ],
    'demo':[
        'demo/estate_property_type_demo.xml',
        'demo/real_estate_property_demo.xml',
        ],
    'assets':{
        'web.assets_frontend':[
            'real_estate/static/src/scss/main.scss'
        ],
        'website.assets_wysiwyg': [
          
            'real_estate/static/src/js/options.js',
        ],
    },
    'summary':'A real estate module',
   'installable':'true',
   'application':'true',
}
