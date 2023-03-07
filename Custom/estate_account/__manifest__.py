{
    'name': 'Estate Accounting',
    'version': '1.0',
    'depends': ['base',
                'Estate',
                'account',
                ],
    'author': 'Astik singh',
    'description': 'Link module between estate and account modules',
    'data': [
        'security/ir.model.access.csv',
        # 'report/report_inherit.xml'
    ],
    'application': True,
    'installable' :True
}