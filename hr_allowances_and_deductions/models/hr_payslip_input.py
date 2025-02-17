from odoo import api, fields, models


class HrPayslipInput(models.Model):
    _inherit = 'hr.payslip.input'

    from_all_ded = fields.Boolean(string='From All Ded', copy=True, store=True)
