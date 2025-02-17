from odoo import api, fields, models


class AdvanceSalary(models.Model):
    _name = 'advance.salary'
    _description = 'Advance Salary'
    
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
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
    advance_type = fields.Many2one(comodel_name='advance.salary.type', string='Advance Type', copy=True, required=True, ondelete='restrict', store=True)
    amount = fields.Float(string='Amount', copy=True, store=True)
    attachment = fields.Binary(string='Attachment', copy=True, store=True)
    close_date = fields.Date(string='Close Date', readonly=True, store=True)
    commission = fields.Float(string='Commission', copy=True, store=True)
    company_id = fields.Many2one(comodel_name='res.company', string='Company', copy=True, ondelete='cascade', store=True)
    count_journal = fields.Integer(string='Journal Count', readonly=True)
    currency_id = fields.Many2one(comodel_name='res.currency', string='Currency', related='company_id.currency_id', readonly=True, store=True)
    due_date = fields.Date(string='Due Date', copy=True, store=True)
    employee_id = fields.Many2one(comodel_name='hr.employee', string='Employee', copy=True, store=True)
    has_message = fields.Boolean(string='Has Message', readonly=True)
    install_value = fields.Float(string='Installment Value', readonly=True)
    installment_ids = fields.One2many(comodel_name='pay.advance.line', inverse_name='advance_id', string='Installment Lines', store=True)
    is_close = fields.Boolean(string='Is Close', readonly=True)
    is_has_group = fields.Boolean(string='Is Has Group', readonly=True)
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
    name = fields.Char(string='Name', copy=True, store=True)
    num_install = fields.Integer(string='Installment Number', copy=True, store=True)
    on_salary = fields.Boolean(string='Deduct From Salary', copy=True, store=True)
    paid_amount = fields.Float(string='Paid Amount', copy=True, readonly=True, store=True)
    payment_date = fields.Date(string='Payment Date', readonly=True, store=True)
    post_date = fields.Date(string='Post Date', copy=True, store=True)
    remaining = fields.Float(string='Remaining Amount', readonly=True, store=True)
    state = fields.Selection(string='State', selection=[('draft', 'Draft'), ('waiting_hr_approval', 'Waiting Hr Approval'), 
                                                        ('waiting_general_manager_approval', 'Waiting General Manager Approval'), 
                                                        ('confirm', 'Confirm'), ('paid', 'Paid'), ('close', 'Close'), ('cancel', 'Canceled')], 
                                                default='draft', store=True)
    website_message_ids = fields.One2many(comodel_name='mail.message', inverse_name='res_id', string='Website Messages', help="""Website communication history""", store=True)

    def action_confirm(self):
        pass

    def action_cancel(self):
        pass

    def action_submit(self):
        pass

    def action_approve(self):
        pass

    def action_cancel(self):
        pass

    def action_open_order(self):
        pass
