from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    damage_product = fields.Many2one(comodel_name='product.product', string='Damage Product', related='company_id.damage_product', readonly=False)
