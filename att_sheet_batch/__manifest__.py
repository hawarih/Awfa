
{
    'name': 'att_sheet_batch',
    'version': '1.0',
    'summary': 'Auto-generated module for att_sheet_batch',
    'author': 'Generated Script',
    'category': 'Custom',
    'depends': ['base', 'account', 'hr_payroll', 'hr_payroll_account', 'hr_attendance_sheet'],
    'data': [
        'data/res_groups.xml',
        
        'security/ir.model.access.csv',
        
        'views/action_act_window.xml',
        'views/account_account_view.xml',
        'views/account_move_view.xml',
        'views/attendance_sheet_batch_view.xml',
        'views/attendance_sheet_view.xml',
        'views/create_payment_wizard_view.xml',
        'views/hr_employee_view.xml',
        'views/hr_payslip_view.xml',
        'views/menu_items.xml',
],
    'installable': True,
    'application': False,
}
