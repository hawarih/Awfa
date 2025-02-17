
{
    'name': 'registration_num_in_employee',
    'version': '1.0',
    'summary': 'Auto-generated module for registration_num_in_employee',
    'author': 'Generated Script',
    'category': 'Custom',
    'depends': ['base', 'hr', 'additional_naql_fields', 'branch_work_location', 'hijri_date_abstract', 'hr_employee_updation'],
    'data': [
        'data/mail_activity.xml',
        'data/ir_cron.xml',
        
        'security/ir.model.access.csv',
        
        'views/action_act_window.xml',
        'views/hr_contract_view.xml',
        'views/hr_department_view.xml',
        'views/hr_employee_view.xml',
        'views/hr_work_location_view.xml',
        'views/register_number_view.xml',
        'views/res_partner_view.xml',
        'views/menu_items.xml',
        
    ],
    'installable': True,
    'application': False,
}
