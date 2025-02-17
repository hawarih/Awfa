
{
    'name': 'partner_customizations',
    'version': '1.0',
    'summary': 'Auto-generated module for partner_customizations',
    'author': 'Generated Script',
    'category': 'Custom',
    'depends': ['sale', 'purchase', 'account'],
    'data': [
        'data/res_groups.xml',
        
        'views/account_move_views.xml',
        'views/account_payment_views.xml',
        'views/purchase_order_views.xml',
        'views/res_partner_views.xml',
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'application': False,
}
