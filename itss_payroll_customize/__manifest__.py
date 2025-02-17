
{
    'name': 'itss_payroll_customize',
    'version': '1.0',
    'summary': 'Auto-generated module for itss_payroll_customize',
    'author': 'Generated Script',
    'category': 'Custom',
    'depends': [ 'base', 'hr', 'hr_payroll', 'hr_contract', 'hr_attendance_sheet'],
    'data': [
        'security/ir.model.access.csv',
        
        'data/hr_salary_rule.xml',
        
        'views/hr_contract_view.xml',
        'views/hr_other_allowance_view.xml',
        'views/hr_payslip_view.xml',
        'views/action_act_window.xml',
        'views/menu_items.xml',
],
    'installable': True,
    'application': False,
}
