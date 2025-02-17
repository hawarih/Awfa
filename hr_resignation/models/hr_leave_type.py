from odoo import api, fields, models


class HrLeaveType(models.Model):
    _inherit = 'hr.leave.type'

    remove_remaining = fields.Boolean(string='Remove Remaining', copy=True, store=True)
