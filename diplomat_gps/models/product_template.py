from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    gps_ok = fields.Boolean(string='Is GPS', copy=True, store=True)
