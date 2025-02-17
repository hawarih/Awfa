from odoo import api, fields, models


class HrPayslip(models.Model):
    _inherit = 'hr.payslip'

    is_assigned = fields.Boolean(string='Is Assigned', readonly=True)
