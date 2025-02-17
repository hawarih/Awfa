from odoo import api, fields, models


class PettyCashLine(models.Model):
    _name = 'petty.cash.line'
    _description = 'Petty Cash Line'

    amount = fields.Monetary(string='Amount', copy=True, store=True)
    currency_id = fields.Many2one(comodel_name='res.currency', string='Currency', copy=True, store=True)
    invoice_id = fields.Many2one(comodel_name='account.move', string='Invoice', copy=True, store=True)
    name = fields.Char(string='Reference', copy=True, store=True)
    payment_id = fields.Many2one(comodel_name='account.payment', string='Payment', copy=True, store=True)
    petty_adj_id = fields.Many2one(comodel_name='petty.cash.adj', string='Petty Adj', copy=True, store=True)
    petty_id = fields.Many2one(comodel_name='petty.cash', string='Petty Cash', copy=True, store=True)

