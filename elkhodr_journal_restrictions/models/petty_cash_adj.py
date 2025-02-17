from odoo import api, fields, models


class PettyCashAdj(models.Model):
    _inherit = 'petty.cash.adj'

    pay_journal_id = fields.Many2one(comodel_name='account.journal', string='Payment Journal', copy=True, store=True)
