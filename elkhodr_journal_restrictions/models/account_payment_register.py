from odoo import api, fields, models


class AccountPaymentRegister(models.TransientModel):
    _inherit = 'account.payment.register'

    journal_id = fields.Many2one(comodel_name='account.journal', string='Journal', copy=True, store=True)
