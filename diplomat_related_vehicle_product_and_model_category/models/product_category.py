from odoo import api, fields, models


class ProductCategory(models.Model):
    _inherit = 'product.category'

    is_rental_model = fields.Boolean(string='Is Rental Model', copy=True, store=True)
