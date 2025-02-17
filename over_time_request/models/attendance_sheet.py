from odoo import api, fields, models


class AttendanceSheet(models.Model):
    _inherit = 'attendance.sheet'

    no_overtime = fields.Integer(string='No of overtimes', readonly=True, store=True)
    tot_overtime = fields.Float(string='Total Over Time', readonly=True, store=True)
