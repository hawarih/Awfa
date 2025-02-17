from odoo import api, fields, models


class ProductProduct(models.Model):
    _inherit = 'product.product'

    card_ok = fields.Boolean(string='Is Card', copy=True, related='product_tmpl_id.card_ok')
