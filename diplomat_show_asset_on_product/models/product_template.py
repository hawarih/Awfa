from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def action_view_related_assets(self):
        pass
    
    def action_view_related_expense(self):
        pass