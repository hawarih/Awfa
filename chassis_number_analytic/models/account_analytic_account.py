from odoo import api, fields, models


class AccountAnalyticAccount(models.Model):
    _inherit = 'account.analytic.account'

    chassis_num = fields.Char(string='Chassis Number', copy=True, store=True)
