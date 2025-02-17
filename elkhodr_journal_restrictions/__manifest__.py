
{
    'name': 'elkhodr_journal_restrictions',
    'version': '1.0',
    'summary': 'Auto-generated module for elkhodr_journal_restrictions',
    'author': 'Generated Script',
    'category': 'Custom',
    'depends': ['base', 'account', 'sale', 'hr_advance', 'batch_internal_transfer', 'hr_expense', 
                'passion_itss_petty_cash'],
    'data': [        
        'data/category.xml',
        'data/res_groups.xml',
        'data/ir_rule.xml',
        
        'views/account_payment_view.xml',
        'views/batch_internal_transfer_view.xml',
        'views/petty_cash_view.xml',
        'views/res_users_view.xml',
        'views/sale_order_view.xml',
],
    'installable': True,
    'application': False,
}
