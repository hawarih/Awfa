
{
    'name': 'hr_mobile_api',
    'version': '1.0',
    'summary': 'Auto-generated module for hr_mobile_api',
    'author': 'Generated Script',
    'category': 'Custom',
    'depends': ['hr', 'hr_attendance_sheet'],
    'data': [
        'data/res_groups.xml',
        
        'security/ir.model.access.csv',

        'views/action_act_window.xml',
        'views/allowed_attendance_location_view.xml',
        'views/hr_attendance_view.xml',
        'views/mobile_terms_policy_view.xml',
        'views/res_config_settings_view.xml',
        'views/menu_items.xml',
    ],
    'installable': True,
    'application': False,
}
