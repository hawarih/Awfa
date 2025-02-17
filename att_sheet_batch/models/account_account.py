from odoo import api, fields, models


class AccountAccount(models.Model):
    _inherit = 'account.account'

    payslip_partner = fields.Boolean(string='Payslip Partner', copy=True, store=True)
