
{
    'name': 'res_partner_customizations',
    'version': '1.0',
    'summary': 'Auto-generated module for res_partner_customizations',
    'author': 'Generated Script',
    'category': 'Custom',
    'depends': ['base', 'account', 'diplomat_partner_customizations', 'purchase_stock', 'sale', 'purchase', 'account_reports',
                'account_followup', 'calendar'],
    'data': [
        'data/res_groups.xml',
        'views/account_account_view.xml',
        'views/res_partner_view.xml',
    ],
    'installable': True,
    'application': False,
}
