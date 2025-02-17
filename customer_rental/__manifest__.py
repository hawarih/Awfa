
{
    'name': 'customer_rental',
    'version': '1.0',
    'summary': 'Auto-generated module for customer_rental',
    'author': 'Generated Script',
    'category': 'Custom',
    'depends': ['diplomat_partner_customizations', 'base', 'diplomat_vehicle_checklist', 
                'ywt_internal_stock_transfer', 'product', 'fleet', 'account', 'diplomat_vehicle_info',
                'diplomat_gps', 'diplomat_insurance_policy', 'mail', 'stock', 'elkhodr_journal_restrictions'],
    'data': [
        
        'data/category.xml',
        'data/ir_cron.xml',
        'data/res_groups.xml',
        'data/sequence.xml',
        
        'security/ir.model.access.csv',
        
        'views/action_act_window.xml',
        'views/account_move_view.xml',
        'views/add_deduct_wizard_view.xml',
        'views/add_fine_wizard_view.xml',
        'views/confirmation_wizard_view.xml',
        'views/customer_rental_fine_wizard_view.xml',
        'views/customer_rental_plan_view.xml',
        'views/customer_rental_policy_view.xml',
        'views/customer_rental_pricing_view.xml',
        'views/customer_rental_return_wizard_view.xml',
        'views/customer_rental_setting_view.xml',
        'views/extend_contract_payment_wizard_view.xml',
        'views/extend_wizard_view.xml',
        'views/fleet_vehicle_view.xml',
        'views/product_template_view.xml',
        'views/rental_additional_service_view.xml',
        'views/rental_contract_view.xml',
        'views/res_partner_view.xml',
        'views/res_users_view.xml',
        'views/stock_location_view.xml',
        'views/menu_items.xml',
    ],
    
    'assets': {
        'web.assets_backend': [
            # 'customer_rental/static/src/components/**/*',
            'customer_rental/static/src/components/page_control_widget/page_control_widget.xml',
            'customer_rental/static/src/components/page_control_widget/page_control_widget.js',
        ],
    },
    
    'installable': True,
    'application': False,
}
