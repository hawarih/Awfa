
{
    'name': 'stock_report_quantity_by_location',
    'version': '1.0',
    'summary': 'Auto-generated module for stock_report_quantity_by_location',
    'author': 'Generated Script',
    'category': 'Custom',
    'depends': ['product', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        
        'views/stock_report_quantity_by_location_prepare_view.xml',
        'views/stock_report_quantity_by_location_view.xml',
        'views/action_act_window.xml',
        'views/menu_items.xml',
],
    'installable': True,
    'application': False,
}
