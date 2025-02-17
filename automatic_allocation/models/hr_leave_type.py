from odoo import api, fields, models


class HrLeaveType(models.Model):
    _inherit = 'hr.leave.type'

    automatic_allocation = fields.Boolean(string='Automatic Allocation', copy=True, store=True)
