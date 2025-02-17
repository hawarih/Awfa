from odoo import api, fields, models


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    approval_code = fields.Char(string='Approval Code', copy=True, store=True, )
    bypass_intermediate_account = fields.Boolean(string='Bypass Intermediate Account', related='company_id.bypass_intermediate_account', readonly=True)
    enable_payment_method = fields.Boolean(string='Work With Payment Methods', related='journal_id.enable_payment_method', readonly=True, store=True)
    is_internal_transfer_bypass = fields.Boolean(string='Is Internal Transfer', copy=True, store=True, )
    journal_method_id = fields.Many2one(comodel_name='journal.payment.method', string='Journal Payment Method', copy=True, store=True, )
