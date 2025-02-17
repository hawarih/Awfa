from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_oil = fields.Boolean(string='Is Oil', copy=True, store=True)
