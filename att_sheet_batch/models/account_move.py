from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    attendance_sheet_batch_id = fields.Many2one(comodel_name='attendance.sheet.batch', string='Batch', copy=True, store=True)
    hr_payslip_id = fields.Many2one(comodel_name='hr.payslip', string='Hr Payslip', copy=True, store=True)
