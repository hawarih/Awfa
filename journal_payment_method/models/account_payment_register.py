from odoo import api, fields, models


class AccountPaymentRegister(models.TransientModel):
    _inherit = 'account.payment.register'

    approval_code = fields.Char(string='Approval Code', copy=True, store=True)
    enable_payment_method = fields.Boolean(string='Work With Payment Methods', related='journal_id.enable_payment_method', readonly=True, store=True)
    journal_id = fields.Many2one(comodel_name='account.journal', string='Journal', copy=True, store=True)
    journal_method_id = fields.Many2one(comodel_name='journal.payment.method', string='Journal Payment Method', copy=True, store=True)
