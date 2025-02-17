from odoo import api, fields, models


class ProductProduct(models.Model):
    _inherit = 'product.product'

    def action_view_related_assets(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Assets',
            'res_model': 'account.asset',
            'view_mode': 'tree,form',  # Opens the tree view, allows switching to form view
            'domain': [('asset_type', '=', 'purchase'), ('state', '!=', 'model'), ('parent_id', '=', False)],
            'target': 'current',
        }
    
    def action_view_related_expense(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Deferred Expenses',
            'res_model': 'account.asset',
            'view_mode': 'tree,form',  # Opens the tree view, allows switching to form view
            'domain': [('asset_type', '=', 'expense'), ('state', '!=', 'model'), ('parent_id', '=', False)],
            'target': 'current',
        }