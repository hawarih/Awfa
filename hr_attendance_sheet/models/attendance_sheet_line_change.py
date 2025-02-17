from odoo import api, fields, models


class AttendanceSheetLineChange(models.TransientModel):
    _name = 'attendance.sheet.line.change'
    _description = 'Attendance Sheet Line Change'

    att_line_id = fields.Many2one(comodel_name='attendance.sheet.line', string='Att Line', copy=True, store=True)
    diff_time = fields.Float(string='Diff Time', copy=True, store=True)
    late_in = fields.Float(string='Late In', copy=True, store=True)
    note = fields.Text(string='Note', copy=True, required=True, store=True)
    overtime = fields.Float(string='Overtime', copy=True, store=True)

    def change_att_data(self):
        pass