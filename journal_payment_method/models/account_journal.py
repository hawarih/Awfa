from odoo import api, fields, models


class AccountJournal(models.Model):
    _inherit = 'account.journal'

    enable_payment_method = fields.Boolean(string='Work With Payment Methods', copy=True, store=True)
