from odoo import api, fields, models


class AccountJournal(models.Model):
    _inherit = 'account.journal'

    adv_pay_close = fields.Boolean(string='Use in Payment and Close Advance Salary', copy=True, store=True)
