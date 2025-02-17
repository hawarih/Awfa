from odoo import api, fields, models


class YwtInternalStockTransfer(models.Model):
    _inherit = 'ywt.internal.stock.transfer'

    user_allowed_location_ids = fields.Many2many(comodel_name='stock.location', relation="stock_location_allowed_rel", string='User Allowed Location', readonly=True)
    user_location_ids = fields.Many2many(comodel_name='stock.location', relation="user_location_allowed_rel", string='User Location', readonly=True)
