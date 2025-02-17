from odoo import api, fields, models


class HrLeaveType(models.Model):
    _inherit = 'hr.leave.type'

    maximum_request = fields.Integer(string='Maximum Number of Request', copy=True, store=True)
    time_off_cut = fields.Boolean(string='Time off Cut', copy=True, store=True)
    time_off_ticket = fields.Boolean(string='Time off Ticket', copy=True, store=True)
    weekend_included = fields.Boolean(string='Weekend Included', copy=True, store=True)
