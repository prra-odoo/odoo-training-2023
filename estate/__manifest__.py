{
    'name': "Real Estate",
    'version': '1.0',
    'depends': ['base','base_address_extended','mail','website'],
    'author': "Author Name",
    'category': 'Category',
     'license': 'LGPL-3',

    'description': """
    Description text
    """,

        
    'data': [
        "security/ir.model.access.csv",

        "views/estate_property_views.xml",


        "views/estate_property_type_views.xml",
        "views/estate_property_tag_views.xml",
        "views/estate_property_offer_views.xml",
        "report/estate_property_reports.xml",
        "report/estate_property_templates.xml",
        "controllers/templates.xml",
        "controllers/controller_view.xml",


        "views/inherited_model_view.xml",
       
        "views/estate_menus.xml"
        
    ],

    'demo':[
        "demo/demo_data.xml"
        
    ],


    'application': True


}
