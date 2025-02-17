from odoo import api, fields, models


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    journal_ids = fields.Many2many(comodel_name='account.journal', relation="journal_rel", column1='payment_id', column2='journal_id', string='Journal', readonly=True)
    transfer_journal_ids = fields.Many2many(comodel_name='account.journal', relation="transfer_journal_rel", column1='payment_id', column2='journal_id', string='Transfer Journal', readonly=True)
    
    
class AccountJournal(models.Model):
    _inherit = 'account.journal'

    journal_rel = fields.Many2many(comodel_name='account.payment', relation="journal_ids", column1='journal_id', column2='payment_id', string='Journal')
    transfer_journal_rel = fields.Many2many(comodel_name='account.payment', relation="transfer_journal_ids", column1='journal_id', column2='payment_id', string='Transfer Journal')
    