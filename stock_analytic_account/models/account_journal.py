from odoo import api, fields, models


class AccountJournal(models.Model):
    _inherit = 'account.journal'

    use_in_stock = fields.Boolean(string='Use In Stock', copy=True, store=True)
