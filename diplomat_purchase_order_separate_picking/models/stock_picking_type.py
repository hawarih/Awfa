from odoo import api, fields, models


class StockPickingType(models.Model):
    _inherit = 'stock.picking.type'

    separate_picking = fields.Boolean(string='Separate Picking', copy=True, store=True)
