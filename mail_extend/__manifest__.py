{
    'name': 'CRM Extend',
    'version': '1.0',
    'depends': ['base', 'mail', 'crm', 'sale'],
    'author': "Ino",
    'category': 'Test',
    'description': """
        CRM (Activity) extend
    """,
    'data': [
        'views/mail_activity.xml',
        'views/crm_lead.xml',
        'report/mail_activity_report.xml',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
    ]
}