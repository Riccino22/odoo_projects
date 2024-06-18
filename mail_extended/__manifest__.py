{
    'name': 'Extended CRM',
    'version': '1.0',
    'depends': ['base', 'mail', 'crm'],
    'author': "Ino",
    'category': 'Test',
    'description': """
        CRM (Activity Model) extended
    """,
    'data': [
        'views/mail_activity.xml',
        'views/crm_lead.xml',
        'report/mail_activity_report.xml',
        'views/menu_views.xml',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
    ]
}