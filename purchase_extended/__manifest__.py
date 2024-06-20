{
    'name': "Purchase Extended",
    'version': '1.0',
    'depends': ['base', 'purchase'],
    'author': "Riccino",
    'category': 'Category',
    'description': """
    An purchase extension module
    """,

    'data': [
        'views/purchase_order.xml',
        'data/purchase_order_cron.xml'
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
    ],
}