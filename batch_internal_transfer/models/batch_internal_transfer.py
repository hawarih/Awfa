from odoo import api, fields, models


class BatchInternalTransfer(models.Model):
    _name = 'batch.internal.transfer'
    _description = 'Batch Internal Transfer'
    
    _inherit = ['mail.thread', 'mail.activity.mixin']
    

    account_payment_ids = fields.One2many(comodel_name='account.payment', inverse_name='batch_internal_transfer_id', string='Account Payment', store=True)
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
    batch_internal_transfer_line_ids = fields.One2many(comodel_name='batch.internal.transfer.line', inverse_name='batch_internal_transfer_id', string='Batch Internal Transfer Line', store=True)
    date = fields.Date(string='Date', copy=True, store=True)
    has_message = fields.Boolean(string='Has Message', readonly=True)
    journal_id = fields.Many2one(comodel_name='account.journal', string='Transfer To', copy=True, store=True)
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
    name = fields.Char(string='Name', store=True)
    payment_count = fields.Integer(string='Payment Count', readonly=True)
    state = fields.Selection(string='Status', selection=[('draft', 'Draft'), ('waiting_approve', 'Waiting Approve'), 
                                                        ('approved', 'Approved'), ('partial_post', 'Partial Post'), ('posted', 'Posted')], 
                                                default='draft', store=True)
    total_amount = fields.Float(string='Total Amount', readonly=True)
    transfer_from_ids = fields.Many2many(comodel_name='account.journal', string='Transfer From', readonly=True, relation='account_journal_batch_internal_transfer_rel', column1='batch_internal_transfer_id', column2='account_journal_id', store=True)
    website_message_ids = fields.One2many(comodel_name='mail.message', inverse_name='res_id', string='Website Messages', help="""Website communication history""", store=True)

    def send_to_auditor(self):
        pass
    
    def action_approve(self):
        pass
    
    def generate_payments(self):
        pass
    
    def action_view_payment(self):
        pass

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('batch') or 'New'
        return super(BatchInternalTransfer, self).create(vals)