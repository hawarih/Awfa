from odoo import api, fields, models


class AttendanceSheetLine(models.Model):
    _name = 'attendance.sheet.line'
    _description = 'Attendance Sheet Line'

    ac_sign_in = fields.Float(string='Actual sign in', copy=True, readonly=True, store=True)
    ac_sign_out = fields.Float(string='Actual sign out', copy=True, readonly=True, store=True)
    att_sheet_id = fields.Many2one(comodel_name='attendance.sheet', string='Attendance Sheet', copy=True, readonly=True, store=True)
    date = fields.Date(string='Date', copy=True, store=True)
    day = fields.Selection(string='Day of Week', selection=[('0', 'Monday'), ('1', 'Tuesday'), ('2', 'Wednesday'), ('3', 'Thursday'), ('4', 'Friday'), ('5', 'Saturday'), ('6', 'Sunday')], copy=True, required=True, index=True, store=True)
    diff_time = fields.Float(string='Diff Time', help="""Diffrence between the working time and attendance time(s) """, copy=True, readonly=True, store=True)
    late_in = fields.Float(string='Late In', copy=True, readonly=True, store=True)
    note = fields.Text(string='Note', copy=True, readonly=True, translate=True, store=True)
    overtime = fields.Float(string='Overtime', copy=True, readonly=True, store=True)
    pl_sign_in = fields.Float(string='Planned sign in', copy=True, readonly=True, store=True)
    pl_sign_out = fields.Float(string='Planned sign out', copy=True, readonly=True, store=True)
    state = fields.Selection(string='State', selection=[('draft', 'Draft'), ('confirm', 'Confirmed'), ('done', 'Approved')], 
                                                default='draft', readonly=True, store=True)
    status = fields.Selection(string='Status', selection=[('ab', 'Absence'), ('weekend', 'Week End'), ('ph', 'Public Holiday'), ('leave', 'Leave'), ('unpaid_leave', 'Unpaid Leave'), ('late', 'Late'), ('overtime', 'Overtime'), ('difference', 'Difference'), ('late_and_difference', 'Late&Difference'), ('late_and_overtime', 'Late&Overtime')], copy=True, readonly=True, store=True)
    worked_hours = fields.Float(string='Worked Hours', copy=True, readonly=True, store=True)
    