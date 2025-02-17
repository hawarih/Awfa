from odoo import api, fields, models


class PurchaseType(models.Model):
    _inherit = 'purchase.type'

    separate_stock_picking = fields.Boolean(string='Separate Stock Picking', copy=True, store=True)
