from odoo import api, fields, models


class PettyCash(models.Model):
    _inherit = 'petty.cash'

    account_journal_ids = fields.Many2many(comodel_name='account.journal', string='Account Journal', readonly=True)
