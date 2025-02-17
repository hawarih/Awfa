from odoo import api, fields, models


class StockLot(models.Model):
    _inherit = 'stock.lot'

    active = fields.Boolean(string='Active', copy=True, store=True)
