{
    'name': 'Help Desk Extended',
    'version': '1.0',
    'depends': ['base', 'helpdesk_mgmt'],
    'author': "Riccino",
    'category': 'Test',
    'description': """
        Helpdesk extended
    """,
    'data': [
        'security/ir.model.access.csv',
        'views/category_sug_form_template.xml',
        'views/helpdesk_category_sug.xml',
        'views/helpdesk_category_sug_menu.xml',
        'views/category_sug_sended_template.xml',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
    ],
    
    'installable': True,
    'application': False,
}