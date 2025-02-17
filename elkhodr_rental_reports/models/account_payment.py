from odoo import api, fields, models


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    description = fields.Char(string='Description', copy=True, store=True)
    word_num = fields.Char(string='Amount In Words:', readonly=True, translate=True)
