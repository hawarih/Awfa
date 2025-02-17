from odoo import api, fields, models


class StockPickingType(models.Model):
    _inherit = 'stock.picking.type'

    show_in_requisition = fields.Boolean(string='Show In Requisition', copy=True, store=True)
