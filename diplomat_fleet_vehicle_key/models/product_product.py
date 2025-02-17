from odoo import api, fields, models


class ProductProduct(models.Model):
    _inherit = 'product.product'

    is_key = fields.Boolean(string='Is Key', copy=True, related='product_tmpl_id.is_key')
    key_type = fields.Selection(string='Key Type', selection=[], copy=True, related='product_tmpl_id.key_type')
