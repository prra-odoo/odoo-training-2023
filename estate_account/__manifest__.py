{
    'name': 'Estate Account',
    'version': '2.0',
    'description': 'Estate Account Module',
    'author': 'odoo',
    'category': 'marketing',
    'installable': True, 
    'summary': 'Estate Account i.e  linked to the real estate', 
    'application': True,
    
    'depends': [
        'real_estate','account'

    ],
    'demo':[
        
    ],
    
    'data': [
                        
        'report/account_report.xml'
     ],
'auto_install': False  

}