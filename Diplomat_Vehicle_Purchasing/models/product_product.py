from odoo import api, fields, models


class ProductProduct(models.Model):
    _inherit = 'product.product'

    supplier_taxes_id = fields.Many2many(comodel_name='account.tax', string='Vendor Taxes', help="""Default taxes used when buying the product.""", copy=True, related='product_tmpl_id.supplier_taxes_id')
