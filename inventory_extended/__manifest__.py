{
    'name': 'Inventory Extended',
    'version': '1.0',
    'depends': ['base', 'stock'],
    'author': "Riccino",
    'category': 'Test',
    'description': """
        Helpdesk extended
    """,
    'data': [
        'security/ir.model.access.csv',
        'wizard/generate_price_product_view.xml',
        'views/product_template.xml'
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
    ],
    
    'installable': True,
    'application': False,
}