from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    supplier_taxes_id = fields.Many2many(comodel_name='account.tax', string='Vendor Taxes', help="""Default taxes used when buying the product.""", copy=True, relation='product_supplier_taxes_rel', column1='prod_id', column2='tax_id', store=True)
