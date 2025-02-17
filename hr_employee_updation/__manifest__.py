
{
    'name': 'hr_employee_updation',
    'version': '1.0',
    'summary': 'Auto-generated module for hr_employee_updation',
    'author': 'Generated Script',
    'category': 'Custom',
    'depends': ['hr', 'hr_contract', 'base', 'mail', 'hr_gamification'],
    'data': [
        'data/hr_employee_relation.xml',
        'data/ir_cron.xml',
        
        'security/ir.model.access.csv',

        'views/action_act_window.xml',
        'views/hr_contract_view.xml',
        'views/hr_employee_view.xml',
        'views/res_config_settings_view.xml',
        'views/menu_items.xml',
    ],
    'installable': True,
    'application': False,
}
