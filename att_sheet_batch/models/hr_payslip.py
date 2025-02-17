from odoo import api, fields, models


class HrPayslip(models.Model):
    _inherit = 'hr.payslip'

    attendance_sheet_batch_id = fields.Many2one(comodel_name='attendance.sheet.batch', string='Attendance Sheet Batch', copy=True, store=True)
    move_state = fields.Selection(string='Journal Entry Status', selection=[], related='move_id.state', readonly=True, )
