
{
    'name': 'sick_leave_saudi_arabia',
    'version': '1.0',
    'summary': 'Auto-generated module for sick_leave_saudi_arabia',
    'author': 'Generated Script',
    'category': 'Custom',
    'depends': ['base', 'hr', 'hr_contract', 'hr_payroll', 'hr_holidays', 'hr_attendance_sheet'],
    'data': [
        'security/ir.model.access.csv',
        
        'data/hr_salary_rule.xml',
        
        'views/hr_contract_view.xml',
        'views/hr_leave_type_view.xml',
],
    'installable': True,
    'application': False,
}
