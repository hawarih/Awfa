from odoo import api, fields, models


class AccountTax(models.Model):
    _inherit = 'account.tax'

    use_po = fields.Boolean(string='Use With PO', copy=True, store=True)
