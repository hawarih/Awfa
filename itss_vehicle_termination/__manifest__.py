
{
    'name': 'itss_vehicle_termination',
    'version': '1.0',
    'summary': 'Auto-generated module for itss_vehicle_termination',
    'author': 'Generated Script',
    'category': 'Custom',
    'depends': ['sale_management', 'diplomat_show_asset_on_product', 'diplomat_insurance_policy'],
    'data': [
        'data/sequence.xml',
        
        'security/ir.model.access.csv',

        'views/action_act_window.xml',
        'views/account_move_view.xml',
        'views/res_config_settings_view.xml',
        'views/stock_lot_view.xml',
        'views/vehicle_termination_view.xml',
        'views/menu_items.xml',
    ],
    'installable': True,
    'application': False,
}
