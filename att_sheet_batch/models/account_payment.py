from odoo import api, fields, models


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    attendance_sheet_batch_id = fields.Many2one(comodel_name='attendance.sheet.batch', string='Batch', copy=True, related='move_id.attendance_sheet_batch_id')
    hr_payslip_id = fields.Many2one(comodel_name='hr.payslip', string='Hr Payslip', copy=True, related='move_id.hr_payslip_id')
