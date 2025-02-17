
{
    'name': 'diplomat_purchase_order_separate_picking',
    'version': '1.0',
    'summary': 'Auto-generated module for diplomat_purchase_order_separate_picking',
    'author': 'Generated Script',
    'category': 'Custom',
    'depends': ['stock', 'Diplomat_Vehicle_Purchasing', 'purchase', 'base'],
    'data': [
        'security/ir.model.access.csv',
        
        'views/action_act_window.xml',
        'views/purchase_order_view.xml',
        'views/purchase_type_view.xml',
        'views/separate_picking_view.xml',
        'views/stock_picking_type_view.xml',
],
    'installable': True,
    'application': False,
}
