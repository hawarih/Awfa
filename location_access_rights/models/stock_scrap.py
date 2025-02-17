from odoo import api, fields, models


class StockScrap(models.Model):
    _inherit = 'stock.scrap'

    user_location_ids = fields.Many2many(comodel_name='stock.location', relation="location_stock_scrap_rel", string='User Location', readonly=True)
