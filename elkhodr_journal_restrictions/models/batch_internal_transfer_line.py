from odoo import api, fields, models


class BatchInternalTransferLine(models.Model):
    _inherit = 'batch.internal.transfer.line'

    journal_ids = fields.Many2many(comodel_name='account.journal', string='Journal', readonly=True)
