
{
    'name': 'adjustment_docs',
    'version': '1.0',
    'summary': 'Auto-generated module for adjustment_docs',
    'author': 'Generated Script',
    'category': 'Custom',
    'depends': ['base', 'hr', 'employee_documents_expiry', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        
        'data/ir_cron.xml',
        'data/mail_activity.xml',
        'views/hr_employee_document_view.xml',
        'views/hr_employee_view.xml',
        'views/action_server.xml',
],
    'installable': True,
    'application': False,
}
