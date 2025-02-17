
{
    'name': 'hr_attendance_sheet',
    'version': '1.0',
    'summary': 'Auto-generated module for hr_attendance_sheet',
    'author': 'Generated Script',
    'category': 'Custom',
    'depends': ['base', 'hr', 'hr_holidays', 'hr_payroll', 'hr_attendance', 'l10n_sa_hr_payroll'],
    'data': [
        'data/category.xml',
        'data/res_groups.xml',
        'data/hr_leave_type.xml',
        'data/hr_payroll_structure_type.xml',
        'data/hr_payroll_structure.xml',
        'data/hr_salary_rule.xml',
        'data/hr_work_entry_type.xml',
        
        'security/ir.model.access.csv',
        
        'reports/report_paperformat.xml',
        
        'views/attendance_sheet_line_change_view.xml',
        'views/attendance_sheet_view.xml',
        'views/hr_absence_rule_view.xml',
        'views/hr_attendance_policy_view.xml',
        'views/hr_contract_view.xml',
        'views/hr_diff_rule_view.xml',
        'views/hr_employee_view.xml',
        'views/hr_late_rule_view.xml',
        'views/hr_overtime_rule_view.xml',
        'views/hr_public_holiday_view.xml',
        'views/action_act_window.xml',
        'views/menu_items.xml',
],
    'installable': True,
    'application': False,
}
