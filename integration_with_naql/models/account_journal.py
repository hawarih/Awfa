from odoo import api, fields, models


class AccountJournal(models.Model):
    _inherit = 'account.journal'

    naql_payment_method_code = fields.Char(string='Naql Payment Method Code', copy=True, store=True)
