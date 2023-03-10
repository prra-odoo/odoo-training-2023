{
    "name":"Estate",
    "depends" : ["website"],
    "installable" : True,
    "application" : True,
    "category" : "Real Estate/Brokerage",
    "data" : [
        "security/ir.model.access.csv",
        "security/security.xml",
        "demo/demo_data.xml",
        "views/estate_property_views.xml",
        "views/estate_property_offer_views.xml",
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',
        "views/estate_menus.xml",
        "views/res_users_views.xml",
        "report/estate_property_templates.xml",
        "report/estate_property_reports.xml",
        "wizard/offer_wizard_views.xml"
    ]
}