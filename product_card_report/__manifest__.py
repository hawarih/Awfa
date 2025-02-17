
{
    'name': 'product_card_report',
    'version': '1.0',
    'summary': 'Auto-generated module for product_card_report',
    'author': 'Generated Script',
    'category': 'Custom',
    'depends': ['stock', 'stock_account', 'stock_report_quantity_by_location'],
    'data': [
        'security/ir.model.access.csv',
        
        'views/action_act_window.xml',
        'views/product_card_report_layout.xml',
        'views/product_card_report_wizard_view.xml',
        'views/product_card_tmp_report.xml',
        'views/product_template_view.xml',
],
    'installable': True,
    'application': False,
}
