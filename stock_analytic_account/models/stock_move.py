from odoo import api, fields, models


class StockMove(models.Model):
    _inherit = 'stock.move'

    analytic_account_ids = fields.Many2many(comodel_name='account.analytic.account', string='Analytic Account', copy=True, relation='account_analytic_account_stock_move_rel', column1='stock_move_id', column2='account_analytic_account_id', store=True)
    analytic_distribution = fields.Json(string='Analytic Distribution', copy=True, store=True)
    analytic_precision = fields.Integer(string='Analytic Precision', copy=True)
