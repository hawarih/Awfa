from odoo import api, fields, models


class AccountAccount(models.Model):
    _inherit = 'account.account'

    allowed_with_customer = fields.Boolean(string='Allowed With Customer', copy=True, store=True)
    allowed_with_vendor = fields.Boolean(string='Allowed With Vendor', copy=True, store=True)
