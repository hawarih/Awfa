
{
    'name': 'hr_advance',
    'version': '1.0',
    'summary': 'Auto-generated module for hr_advance',
    'author': 'Generated Script',
    'category': 'Custom',
    'depends': ['base', 'account', 'hr', 'sale', 'hr_payroll'],
    'data': [
        
        'data/category.xml',
        'data/res_groups.xml',
        'data/sequence.xml',
        
        'security/ir.model.access.csv',
        
        'views/account_journal_view.xml',
        'views/action_act_window.xml',
        'views/advance_salary_view.xml',
        'views/advance_salary_type_view.xml',
        'views/hr_employee_view.xml',
        'views/menu_items.xml',
        
        'wizard/close_advances_view.xml',
        'wizard/close_wizard_view.xml',
        'wizard/pay_wizard_view.xml',
],
    'installable': True,
    'application': False,
}
