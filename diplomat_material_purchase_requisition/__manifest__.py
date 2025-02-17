
{
    'name': 'diplomat_material_purchase_requisition',
    'version': '1.0',
    'summary': 'Auto-generated module for diplomat_material_purchase_requisition',
    'author': 'Generated Script',
    'category': 'Custom',
    'depends': ['base', 'hr', 'stock', 'purchase', 'diplomat_partner_customizations'],
    'data': [
        'security/ir.model.access.csv',
        
        'data/category.xml',
        'data/res_groups.xml',
        'data/ir_rule.xml',
        'data/mail_template.xml',
        'data/sequence.xml',
        
        'reports/diplomat_material_purchase_requisition_purchase_requisition.xml',
        
        'views/stock_picking_view.xml',
        'views/res_users_view.xml',
        'views/material_purchase_requisition_view.xml',
        'views/action_act_window.xml',
        'views/menu_items.xml',
],
    'installable': True,
    'application': False,
}
