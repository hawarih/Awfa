from odoo import api, fields, models


class HrLeaveType(models.Model):
    _inherit = 'hr.leave.type'

    sick_leave = fields.Boolean(string='Sick Leave', copy=True, store=True)
