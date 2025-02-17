
{
    'name': 'location_access_rights',
    'version': '1.0',
    'summary': 'Auto-generated module for location_access_rights',
    'author': 'Generated Script',
    'category': 'Custom',
    'depends': ['fleet', 'stock_adjustment', 'base', 'diplomat_purchase_order_separate_picking', 'ywt_internal_stock_transfer',
                'stock', 'customer_rental', 'product', 'diplomat_gps', 'purchase', 'sale', 'sale_stock',
                'stock_report_quantity_by_location'],
    'data': [
        
        'data/category.xml',
        'data/res_groups.xml',
        'data/ir_rule.xml',
                
        'views/customer_rental_return_wizard_view.xml',
        'views/purchase_order_view.xml',
        'views/rental_contract_view.xml',
        'views/res_users_view.xml',
        'views/sale_order_view.xml',
        'views/separate_picking_view.xml',
        'views/stock_inventory_view.xml',
        'views/stock_report_quantity_by_location_prepare_view.xml',
        'views/stock_scrap_view.xml',
        'views/ywt_internal_stock_transfer_view.xml',
],
    'installable': True,
    'application': False,
}
