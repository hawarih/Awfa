from odoo import api, fields, models


class HrEmployeePublic(models.Model):
    _inherit = 'hr.employee.public'

    account_number = fields.Char(string='Account Number', copy=True, store=True)
