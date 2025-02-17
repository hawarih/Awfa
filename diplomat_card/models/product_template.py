from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    card_ok = fields.Boolean(string='Is Card', copy=True, store=True)
