from odoo import api, fields, models


class AttendanceSheet(models.Model):
    _inherit = 'attendance.sheet'

    batch_id = fields.Many2one(comodel_name='attendance.sheet.batch', string='Attendance Sheet Batch', copy=True, store=True)
    struct_id = fields.Many2one(comodel_name='hr.payroll.structure', string='Structure', copy=True, store=True)
