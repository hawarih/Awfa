from odoo import api, fields, models


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    account_number = fields.Char(string='Account Number', copy=True, store=True)
