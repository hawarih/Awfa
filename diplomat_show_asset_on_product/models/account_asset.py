from odoo import api, fields, models


class AccountAsset(models.Model):
    _inherit = 'account.asset'

    product_name = fields.Char(string='Product Name', readonly=True)

    def action_view_related_products(self):
        pass