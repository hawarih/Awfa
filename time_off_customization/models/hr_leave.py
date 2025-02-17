from odoo import api, fields, models


class HrLeave(models.Model):
    _inherit = 'hr.leave'

    check_completion_canceled = fields.Boolean(string='Check Completion Canceled', readonly=True)
    check_cut = fields.Boolean(string='check', readonly=True)
    count_time_off_completion = fields.Integer(string='Count', readonly=True)
    cut_reason = fields.Char(string='Cut Reason', copy=True, store=True, )
    return_date = fields.Date(string='Return Date', copy=True, store=True, )
    time_off_cut = fields.Boolean(string='Time off Cut', related='holiday_status_id.time_off_cut', readonly=True)
    time_off_ticket = fields.Boolean(string='Time off Ticket', related='holiday_status_id.time_off_ticket', readonly=True)

    def action_time_off_cut(self):
        pass

    def action_time_off_ticket(self):
        pass
    
    def action_open_time_off_completion(self):
        pass

