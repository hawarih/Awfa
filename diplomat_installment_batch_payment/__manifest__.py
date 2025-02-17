
{
    'name': 'diplomat_installment_batch_payment',
    'version': '1.0',
    'summary': 'Auto-generated module for diplomat_installment_batch_payment',
    'author': 'Generated Script',
    'category': 'Custom',
    'depends': ['base', 'purchase', 'Diplomat_Vehicle_Purchasing', 'fleet'],
    'data': [
        'data/sequence.xml',
        
        'security/ir.model.access.csv',
        
        'views/action_act_window.xml',
        'views/installment_batch_payment_view.xml',
        'views/menu_items.xml',
],
    'installable': True,
    'application': False,
}
