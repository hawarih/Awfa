
{
    'name': 'hr_resignation',
    'version': '1.0',
    'summary': 'Auto-generated module for hr_resignation',
    'author': 'Generated Script',
    'category': 'Custom',
    'depends': ['mail', 'hr', 'hr_employee_updation', 'passion_itss_petty_cash', 'hr_payroll', 'hr_advance', 
                'hr_allowances_and_deductions', 'hr_payroll_account', 'hr_holidays'],
    'data': [
        'data/category.xml',
        'data/ir_rule.xml',
        'data/ir_sequence.xml',
        'data/mail_activity.xml',
        'data/ir_cron.xml',
        'data/res_groups.xml',
        
        'security/ir.model.access.csv',
        
        'views/action_act_window.xml',
        'views/account_analytic_plan_view.xml',
        'views/hr_employee_view.xml',
        'views/hr_eos_resignation_view.xml',
        'views/hr_leave_type_view.xml',
        'views/hr_payroll_structure_view.xml',
        'views/hr_payslip_view.xml',
        'views/hr_resignation_reason_view.xml',
        'views/hr_resignation_view.xml',
        'views/menu_items.xml',
    ],
    'installable': True,
    'application': False,
}
