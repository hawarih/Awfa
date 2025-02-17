
{
    'name': 'diplomat_insurance_policy',
    'version': '1.0',
    'summary': 'Auto-generated module for diplomat_insurance_policy',
    'author': 'Generated Script',
    'category': 'Custom',
    'depends': ['account_asset', 'diplomat_related_vehicle_product_and_model_category',
                'fleet_analytic_account', 'account_accountant', 'purchase'],
    'data': [
        
        'data/category.xml',
        'data/res_groups.xml',
        'data/ir_cron.xml',
        
        'security/ir.model.access.csv',
        
        'views/fleet_vehicle_view.xml',
        'views/insurance_policy_view.xml',
        'views/po_insurance_line_view.xml',
        'views/purchase_order_line_view.xml',
        'views/purchase_order_view.xml',
        'views/res_config_settings_view.xml',
        'views/action_act_window.xml',
        'views/menu_items.xml',
],
    'installable': True,
    'application': False,
}
