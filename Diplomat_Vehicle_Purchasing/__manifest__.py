
{
    'name': 'Diplomat_Vehicle_Purchasing',
    'version': '1.0',
    'summary': 'Auto-generated module for Diplomat_Vehicle_Purchasing',
    'author': 'Generated Script',
    'category': 'Custom',
    'depends': ['account', 'fleet', 'purchase', 'purchase_stock', 'diplomat_insurance_policy', 
                'diplomat_vehicle_info', 'diplomat_related_vehicle_product_and_model_category'],
    'data': [
        
        'data/category.xml',
        'data/res_groups.xml',
        
        'security/ir.model.access.csv',
        
        'views/action_act_window.xml',
        'views/bill_information_wizard_view.xml',
        'views/create_vehicle_wizard_view.xml',
        'views/purchase_order_view.xml',
        'views/account_move_view.xml',
        'views/leasing_payment_view.xml',
        'views/po_insurance_line.xml',
        'views/purchase_type_view.xml',
        'views/fleet_vehicle_view.xml',
        'views/account_tax_view.xml',
        'views/menu_items.xml',
],
    'installable': True,
    'application': False,
}
