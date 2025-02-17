
{
    'name': 'employee_documents_expiry',
    'version': '1.0',
    'summary': 'Auto-generated module for employee_documents_expiry',
    'author': 'Generated Script',
    'category': 'Custom',
    'depends': ['base', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        
        'data/ir_cron.xml',
        
        'views/employee_checklist_view.xml',
        'views/hr_employee_document_view.xml',
        'views/hr_employee_view.xml',
        'views/action_server.xml',
],
    'installable': True,
    'application': False,
}
