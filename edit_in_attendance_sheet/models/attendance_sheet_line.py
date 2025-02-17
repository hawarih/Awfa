from odoo import api, fields, models


class AttendanceSheetLine(models.Model):
    _inherit = 'attendance.sheet.line'

    day_period = fields.Selection(string='Day Period', selection=[('morning', 'Morning'), ('afternoon', 'Afternoon')], readonly=True)
    difference = fields.Float(string='Absence Time', readonly=True, store=True)
    status = fields.Selection(string='Status', selection=[('ab', 'Absence'), ('weekend', 'Week End'), ('ph', 'Public Holiday'), ('leave', 'Leave'), ('unpaid_leave', 'Unpaid Leave'), ('late', 'Late'), ('overtime', 'Overtime'), ('difference', 'Difference'), ('late_and_difference', 'Late&Difference'), ('late_and_overtime', 'Late&Overtime')], copy=True, readonly=True, store=True)
