from odoo import api, fields, models


class StockLocation(models.Model):
    _inherit = 'stock.location'

    account_analytic_account_id = fields.Many2one(comodel_name='account.analytic.account', string='Account Analytic Account', copy=True, store=True)
    rental_location = fields.Boolean(string='Rental Location', copy=True, store=True)
    sales_journal_id = fields.Many2one(comodel_name='account.journal', string='Sales Journal', copy=True, store=True)
