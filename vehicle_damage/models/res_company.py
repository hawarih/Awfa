from odoo import api, fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    damage_product = fields.Many2one(comodel_name='product.product', string='Damage Product', copy=True, store=True)
