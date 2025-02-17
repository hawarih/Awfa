from odoo import api, fields, models


class HrLeaveCompletion(models.Model):
    _name = 'hr.leave.completion'
    _description = 'Hr Leave Completion'

    activity_calendar_event_id = fields.Many2one(comodel_name='calendar.event', string='Next Activity Calendar Event', readonly=True)
    activity_date_deadline = fields.Date(string='Next Activity Deadline', readonly=True)
    activity_exception_decoration = fields.Selection(string='Activity Exception Decoration', help="""Type of the exception activity on record.""", selection=[('warning', 'Alert'), ('danger', 'Error')], readonly=True)
    activity_exception_icon = fields.Char(string='Icon', help="""Icon to indicate an exception activity.""", readonly=True)
    activity_ids = fields.One2many(comodel_name='mail.activity', inverse_name='res_id', string='Activities', store=True)
    activity_state = fields.Selection(string='Activity State', help="""Status based on activities
Overdue: Due date is already passed
Today: Activity date is today
Planned: Future activities.""", selection=[('overdue', 'Overdue'), ('today', 'Today'), ('planned', 'Planned')], readonly=True)
    activity_summary = fields.Char(string='Next Activity Summary', related='activity_ids.summary')
    activity_type_icon = fields.Char(string='Activity Type Icon', help="""Font awesome icon e.g. fa-tasks""", related='activity_ids.icon', readonly=True)
    activity_type_id = fields.Many2one(comodel_name='mail.activity.type', string='Next Activity Type', related='activity_ids.activity_type_id')
    activity_user_id = fields.Many2one(comodel_name='res.users', string='Responsible User', related='activity_ids.user_id')
    amount = fields.Monetary(string='Amount', readonly=True)
    count_journal_entries = fields.Integer(string='Count', readonly=True)
    count_payments = fields.Integer(string='Count', readonly=True)
    currency_id = fields.Many2one(comodel_name='res.currency', string='Currency', readonly=True, store=True)
    date_from = fields.Date(string='From', copy=True, store=True, )
    date_to = fields.Date(string='To', copy=True, store=True, )
    description = fields.Char(string='Description', copy=True, store=True, )
    duration = fields.Float(string='Duration', copy=True, store=True, )
    employee_id = fields.Many2one(comodel_name='hr.employee', string='Employee', copy=True, store=True, )
    has_message = fields.Boolean(string='Has Message', readonly=True)
    holiday_status_id = fields.Many2one(comodel_name='hr.leave.type', string='Time Off Type', copy=True, store=True)
    leave_id = fields.Many2one(comodel_name='hr.leave', string='Time off', copy=True, store=True, )
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True)
    message_follower_ids = fields.One2many(comodel_name='mail.followers', inverse_name='res_id', string='Followers', store=True)
    message_has_error = fields.Boolean(string='Message Delivery error', help="""If checked, some messages have a delivery error.""", readonly=True)
    message_has_error_counter = fields.Integer(string='Number of errors', help="""Number of messages with delivery error""", readonly=True)
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', help="""If checked, some messages have a delivery error.""", readonly=True)
    message_ids = fields.One2many(comodel_name='mail.message', inverse_name='res_id', string='Messages', store=True)
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True)
    message_main_attachment_id = fields.Many2one(comodel_name='ir.attachment', string='Main Attachment', store=True)
    message_needaction = fields.Boolean(string='Action Needed', help="""If checked, new messages require your attention.""", readonly=True)
    message_needaction_counter = fields.Integer(string='Number of Actions', help="""Number of messages requiring action""", readonly=True)
    message_partner_ids = fields.Many2many(comodel_name='res.partner', string='Followers (Partners)')
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True)
    name = fields.Char(string='Reference', required=True, readonly=True, store=True)
    state = fields.Selection(string='Status', selection=[('draft', 'Draft'), ('submitted', 'Submitted'), ('approved', 'Approved'), 
                                                         ('paid', 'Paid'), ('cancel', 'Cancel')], readonly=True, index=True, 
                                                default='draft', store=True, )
    time_off_allowance = fields.Float(string='Time off Allowance', copy=True, store=True, )
    time_off_amount_ticket = fields.Float(string='Time off Ticket', readonly=True, )
    time_off_other_allowance = fields.Float(string='Time off Other Allowance', copy=True, store=True, )
    time_off_ticket = fields.Float(string='Time off Ticket', copy=True, store=True, )
    total_time_off_allowance = fields.Float(string='Total Time off Allowance', readonly=True, )
    website_message_ids = fields.One2many(comodel_name='mail.message', inverse_name='res_id', string='Website Messages', help="""Website communication history""", store=True)
    work_days = fields.Integer(string='Work Days', copy=True, store=True, )

    def action_submit(self):
        pass

    def action_approve(self):
        pass

    def action_compute_time_off(self):
        pass

    def action_paid(self):
        pass

    def action_cancel(self):
        pass

    def action_open_journal_entries(self):
        pass

    def action_open_payments(self):
        pass
