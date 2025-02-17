
{
    'name': 'hr_allowances_and_deductions',
    'version': '1.0',
    'summary': 'Auto-generated module for hr_allowances_and_deductions',
    'author': 'Generated Script',
    'category': 'Custom',
    'depends': ['base', 'hr', 'hr_payroll'],
    'data': [
        'security/ir.model.access.csv',
        
        'data/category.xml',
        'data/mail_activity_type.xml',
        'data/res_groups.xml',
        'data/sequence.xml',
        
        'views/action_act_window.xml',
        'views/allowance_deduction_view.xml',
        'views/hr_payslip_input_type_view.xml',
        'views/menu_items.xml',
    ],
    'installable': True,
    'application': False,
}
