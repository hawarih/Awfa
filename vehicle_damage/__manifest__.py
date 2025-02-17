
{
    'name': 'vehicle_damage',
    'version': '1.0',
    'summary': 'Auto-generated module for vehicle_damage',
    'author': 'Generated Script',
    'category': 'Custom',
    'depends': ['vehicle_accident', 'base', 'fleet', 'mail', 'customer_rental'],
    'data': [
        'security/ir.model.access.csv',
        
        'data/category.xml',
        'data/res_groups.xml',
        
        'views/action_act_window.xml',
        'views/fleet_vehicle_view.xml',
        'views/menu_items.xml',
        'views/res_config_settings_view.xml',
        'views/vehicle_damage_view.xml',
],
    'installable': True,
    'application': False,
}
