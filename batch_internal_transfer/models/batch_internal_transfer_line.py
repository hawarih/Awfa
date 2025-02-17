from odoo import api, fields, models


class BatchInternalTransferLine(models.Model):
    _name = 'batch.internal.transfer.line'
    _description = 'Batch Internal Transfer Line'

    amount = fields.Float(string='Amount', copy=True, store=True)
    batch_internal_transfer_id = fields.Many2one(comodel_name='batch.internal.transfer', string='Batch Internal Transfer', copy=True, store=True)
    current_balance = fields.Float(string='Current Balance', related='journal_id.default_account_id.current_balance', readonly=True)
    date = fields.Date(string='Date')
    description = fields.Text(string='Description', copy=True, store=True)
    dest_journal_id = fields.Many2one(comodel_name='account.journal', string='Transfer To')
    journal_id = fields.Many2one(comodel_name='account.journal', string='Transfer From', copy=True, store=True)
    state = fields.Selection(string='Status', selection=[('draft', 'Draft'), ('posted', 'Posted')], default='draft', store=True)

    def create_payment(self):
        pass