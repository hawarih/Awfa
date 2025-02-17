from odoo import api, fields, models


class ProductProduct(models.Model):
    _inherit = 'product.product'

    is_spare_part = fields.Boolean(string='Is Spare Part', copy=True, related='product_tmpl_id.is_spare_part')
