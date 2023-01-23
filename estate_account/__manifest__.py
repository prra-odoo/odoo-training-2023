{
    'name': "Estate Account",
    'version': '1.0',
    'depends': ['base','real_estate','account'],
    'author': "Gurpreet Singh(gusi)",
    'category': 'Sales',
    'description': "This is a Real Esate Account App",
    'summary': "This is useful to combine the modules(Accounting and Real Estate)",
    'installable': True,
    'application': True,
    'data': [
        # 'security/ir.model.access.csv',
    ],
    'demo': [
      
    ],
}


# "invoice_line_ids": [
#                         (0,0,{
#                                 "name": prop.name,
#                                 "quantity": 1.0,
#                                 "price_unit": prop.selling_price * 6.0 / 100.0,
#                             },),
#                         (0,0,{
#                                 "name": "Administrative fees",
#                                 "quantity": 1.0,
#                                 "price_unit": 100.0,
#                             },
#                         ),],
#                 }