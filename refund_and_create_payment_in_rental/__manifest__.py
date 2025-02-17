
{
    'name': 'refund_and_create_payment_in_rental',
    'version': '1.0',
    'summary': 'Auto-generated module for refund_and_create_payment_in_rental',
    'author': 'Generated Script',
    'category': 'Custom',
    'depends': ['base', 'customer_rental', 'journal_payment_method'],
    'data': [
        'security/ir.model.access.csv',
        
        'views/customer_payment_wizard_view.xml',
        'views/refund_wizard_view.xml',
        'views/action_act_window.xml',
],
    'installable': True,
    'application': False,
}
