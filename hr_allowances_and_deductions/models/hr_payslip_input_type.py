from odoo import api, fields, models


class HrPayslipInputType(models.Model):
    _inherit = 'hr.payslip.input.type'

    input_times_ids = fields.One2many(comodel_name='input.times', inverse_name='input_type_id', string='Input Times', store=True)
    type = fields.Selection(string='Type', selection=[('allowance', 'Allowance'), ('deduction', 'Deduction')], copy=True, store=True)
