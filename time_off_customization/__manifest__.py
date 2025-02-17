{
    'name': 'time_off_customization',
    'version': '1.0',
    'summary': 'Auto-generated module for time_off_customization',
    'author': 'Generated Script',
    'category': 'Custom',
    'depends': ['att_sheet_batch', 'base', 'hr', 'hr_contract', 'hr_holidays', 'account_accountant'],
    'data': [
        'security/ir.model.access.csv',
        
        'data/sequence.xml',
        
        'views/account_move_view.xml',
        'views/cut_wizard_view.xml',
        'views/hr_contract_view.xml',
        'views/hr_leave_completion_view.xml',
        'views/hr_leave_cut_view.xml',
        'views/hr_leave_type_view.xml',
        'views/hr_leave_view.xml',
        'views/register_payment_view.xml',
        'views/res_config_settings_view.xml',
        'views/action_act_window.xml',
        'views/menu_items.xml',
    ],
    'installable': True,
    'application': False,
}
