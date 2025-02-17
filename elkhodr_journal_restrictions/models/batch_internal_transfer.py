from odoo import api, fields, models


class BatchInternalTransfer(models.Model):
    _inherit = 'batch.internal.transfer'

    transfer_journal_ids = fields.Many2many(comodel_name='account.journal', string='Transfer Journal', relation='account_journal_batch_transfer_rel', column1='batch_internal_transfer_id', column2='journal_id', readonly=True)
