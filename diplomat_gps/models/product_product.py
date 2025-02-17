from odoo import api, fields, models


class ProductProduct(models.Model):
    _inherit = 'product.product'

    gps_ok = fields.Boolean(string='Is GPS', copy=True, related='product_tmpl_id.gps_ok')
