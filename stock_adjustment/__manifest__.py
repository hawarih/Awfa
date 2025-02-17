
{
    'name': 'stock_adjustment',
    'version': '1.0',
    'summary': 'Auto-generated module for stock_adjustment',
    'author': 'Generated Script',
    'category': 'Custom',
    'depends': ['stock_account'],
    'data': [
        'data/mail_activity.xml',
        'data/res_groups.xml',
        
        'security/ir.model.access.csv',

        'reports/stock_adjustment_report_inventory.xml',
        'views/action_act_window.xml',
        'views/stock_inventory_line_view.xml',
        'views/stock_inventory_view.xml',
        'views/menu_items.xml',
    ],
    'installable': True,
    'application': False,
}
