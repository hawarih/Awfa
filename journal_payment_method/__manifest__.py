
{
    'name': 'journal_payment_method',
    'version': '1.0',
    'summary': 'Auto-generated module for journal_payment_method',
    'author': 'Generated Script',
    'category': 'Custom',
    'depends': ['account'],
    'data': [
        'security/ir.model.access.csv',
        
        'views/account_journal_view.xml',
        'views/account_move_line_view.xml',
        'views/account_payment_view.xml',
        'views/journal_payment_method_view.xml',
        'views/res_company_view.xml',
        'views/action_act_window.xml',
        'views/menu_items.xml',
],
    'installable': True,
    'application': False,
}
