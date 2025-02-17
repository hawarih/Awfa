from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_key = fields.Boolean(string='Is Key', copy=True, store=True)
    key_type = fields.Selection(string='Key Type', selection=[('main', 'Main'), ('extra', 'Extra'), ('sub', 'Sub')], copy=True, store=True)
