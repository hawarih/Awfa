from odoo import api, fields, models


class StockInventory(models.Model):
    _inherit = 'stock.inventory'

    user_location_ids = fields.Many2many(comodel_name='stock.location', string='User Location', relation="stock_user_location_rel", readonly=True)
