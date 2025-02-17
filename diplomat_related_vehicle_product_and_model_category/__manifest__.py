
{
    'name': 'diplomat_related_vehicle_product_and_model_category',
    'version': '1.0',
    'summary': 'Auto-generated module for diplomat_related_vehicle_product_and_model_category',
    'author': 'Generated Script',
    'category': 'Custom',
    'depends': ['stock', 'stock_account', 'fleet', 'fleet_analytic_account', 'sale_renting', 'product'],
    'data': [
        'security/ir.model.access.csv',
        
        'views/fleet_vehicle_model_category_view.xml',
        'views/fleet_vehicle_model_view.xml',
        'views/fleet_vehicle_view.xml',
        'views/product_category_view.xml',
        'views/product_template_view.xml',
        'views/usage_type_view.xml',
        'views/action_act_window.xml',
],
    'installable': True,
    'application': False,
}
