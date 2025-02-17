from odoo import api, fields, models


class AttendanceSheet(models.Model):
    _inherit = 'attendance.sheet'

    update_lines = fields.Boolean(string='Update Lines', readonly=True)
