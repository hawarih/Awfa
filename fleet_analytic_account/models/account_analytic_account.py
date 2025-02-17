from odoo import api, fields, models


class AccountAnalyticAccount(models.Model):
    _inherit = 'account.analytic.account'

    is_vehicle = fields.Boolean(string='Is Vehicle', copy=True, store=True)
    serial_number = fields.Char(string='Serial Number', copy=True, store=True)
