from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_spare_part = fields.Boolean(string='Is Spare Part', copy=True, store=True)
