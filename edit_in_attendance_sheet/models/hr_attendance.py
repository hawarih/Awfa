from odoo import api, fields, models


class HrAttendance(models.Model):
    _inherit = 'hr.attendance'

    automatic_check_out = fields.Boolean(string='Automatic Check Out', copy=True, store=True)
