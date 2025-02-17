
{
    'name': 'elkhodr_rental_reports',
    'version': '1.0',
    'summary': 'Auto-generated module for elkhodr_rental_reports',
    'author': 'Generated Script',
    'category': 'Custom',
    'depends': ['base', 'account', 'account_accountant', 'customer_rental'],
    'data': [
        'data/report_paperformat.xml',
        
        'reports/elkhodr_rental_reports_report_batch_internal_transfer.xml',
        'reports/elkhodr_rental_reports_report_receipt.xml',
        'reports/elkhodr_rental_reports_report_rental_contract.xml',
        
        'views/account_payment_view.xml',
        'views/batch_internal_transfer_view.xml',
],
    'installable': True,
    'application': False,
}
