from odoo import api, fields, models


class StockPickingType(models.Model):
    _inherit = 'stock.picking.type'

    show_analytic_distribution = fields.Boolean(string='Show Analytic Distribution', copy=True, store=True)
