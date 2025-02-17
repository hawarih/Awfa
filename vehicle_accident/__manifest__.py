
{
    'name': 'vehicle_accident',
    'version': '1.0',
    'summary': 'Auto-generated module for vehicle_accident',
    'author': 'Generated Script',
    'category': 'Custom',
    'depends': ['base', 'diplomat_insurance_policy', 'mail', 'account', 'customer_rental', 'product', 'fleet', 'maintenance'],
    'data': [
        'security/ir.model.access.csv',
        
        'data/category.xml',
        'data/res_groups.xml',
        'data/sequence.xml',
        
        'views/accident_discount_wizard_view.xml',
        'views/accident_follower_wizard_view.xml',
        'views/diplomat_insurance_policy_view.xml',
        'views/evaluation_party_view.xml',
        'views/fleet_vehicle_view.xml',
        'views/not_insurance_reason_view.xml',
        'views/rental_contract_view.xml',
        'views/res_config_settings_view.xml',
        'views/vehicle_accident_view.xml',
        'views/action_act_window.xml',
        'views/menu_items.xml',
    ],
    'installable': True,
    'application': False,
}
