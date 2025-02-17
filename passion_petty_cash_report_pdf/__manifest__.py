
{
    'name': 'passion_petty_cash_report_pdf',
    'version': '1.0',
    'summary': 'Auto-generated module for passion_petty_cash_report_pdf',
    'author': 'Generated Script',
    'category': 'Custom',
    'depends': ['hr', 'account', 'passion_itss_petty_cash'],
    'data': [
        'security/ir.model.access.csv',

        'views/action_act_window.xml',
        'reports/petty_cash_report_template.xml',
        'views/hr_employee_view.xml',
        'views/petty_report_wizard_view.xml',
        'views/menu_items.xml',
    ],
    'installable': True,
    'application': False,
}
