
{
    'name': 'automatic_allocation',
    'version': '1.0',
    'summary': 'Auto-generated module for automatic_allocation',
    'author': 'Generated Script',
    'category': 'Custom',
    'depends': ['hr_holidays', 'hr_contract'],
    'data': [
        'data/ir_cron.xml',
        
        'views/action_act_window.xml',
        'views/hr_contract_view.xml',
        'views/hr_leave_type_view.xml',
    ],
    'installable': True,
    'application': False,
}
