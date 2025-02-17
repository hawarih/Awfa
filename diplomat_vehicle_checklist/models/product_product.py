from odoo import api, fields, models


class ProductProduct(models.Model):
    _inherit = 'product.product'

    is_oil = fields.Boolean(string='Is Oil', copy=True, related='product_tmpl_id.is_oil')
