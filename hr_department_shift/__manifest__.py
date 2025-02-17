
{
    'name': 'hr_department_shift',
    'version': '1.0',
    'summary': 'Auto-generated module for hr_department_shift',
    'author': 'Generated Script',
    'category': 'Custom',
    'depends': ['base', 'hr', 'hr_contract', 'hr_payroll', 'employee_check_list', 'hijri_date_abstract'],
    'data': [
        'data/category.xml',
        'data/res_groups.xml',
        
        'security/ir.model.access.csv',
        
        'views/hr_contract_view.xml',
        'views/hr_department_shift_lines_view.xml',
        'views/hr_department_view.xml',
        'views/hr_employee_view.xml',
    ],
    'installable': True,
    'application': False,
}
