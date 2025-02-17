from odoo import api, fields, models


class StockPickingType(models.Model):
    _inherit = 'stock.picking.type'

    has_checklist = fields.Boolean(string='Has Checklist', copy=True, store=True)
