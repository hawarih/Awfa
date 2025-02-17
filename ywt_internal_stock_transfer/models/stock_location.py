from odoo import api, fields, models


class StockLocation(models.Model):
    _inherit = 'stock.location'

    allowed_transfer = fields.Boolean(string='Allow Transfer', copy=True, store=True)
