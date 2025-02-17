from odoo import api, fields, models


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    from_stock_picking = fields.Boolean(string='From Stock Picking', copy=True, store=True)
