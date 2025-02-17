
{
    'name': 'ywt_internal_stock_transfer',
    'version': '1.0',
    'summary': 'Auto-generated module for ywt_internal_stock_transfer',
    'author': 'Generated Script',
    'category': 'Custom',
    'depends': ['stock', 'diplomat_related_vehicle_product_and_model_category', 'fleet_status',
                'diplomat_vehicle_checklist', 'fleet', 'diplomat_vehicle_receipt_checklist', 'partner_customizations'],
    'data': [
        
        'data/category.xml',
        'data/mail_activity_type.xml',
        'data/res_groups.xml',
        'data/sequence.xml',
        
        'security/ir.model.access.csv',
        
        'views/ywt_internal_stock_transfer_view.xml',
        'views/action_act_window.xml',
        'views/action_closed_view.xml',
        'views/add_product_view.xml',
        'views/deviation_limit_view.xml',
        'views/res_config_settings_view.xml',
        'views/stock_location_view.xml',
        'views/stock_picking_view.xml',
        'views/stock_quant_view.xml',
        'views/vehicle_checklist_view.xml',
        'views/vehicle_driver_view.xml',
        'views/menu_items.xml',
],
    'installable': True,
    'application': False,
}
