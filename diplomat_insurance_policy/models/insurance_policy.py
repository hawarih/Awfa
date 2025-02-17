from odoo import api, fields, models


class InsurancePolicy(models.Model):
    _name = 'insurance.policy'
    _description = 'Insurance Policy'
    
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
    bill_count = fields.Integer(string='Bills#', readonly=True)
    company_id = fields.Many2one(comodel_name='res.company', string='Company', copy=True, readonly=True, store=True)
    currency_id = fields.Many2one(comodel_name='res.currency', string='Company Currency', help="""Utility field to express amount currency""", related='company_id.currency_id', readonly=True, store=True)
    deductible = fields.Float(string='Deductible', copy=True, store=True)
    end_date = fields.Date(string='End Date', copy=True, required=True, readonly=True, store=True)
    has_message = fields.Boolean(string='Has Message', readonly=True)
    insurance_line_ids = fields.One2many(comodel_name='insurance.policy.line', inverse_name='insurance_id', string='Insurance Lines', store=True)
    insurance_type = fields.Selection(string='Insurance Type', selection=[('full', 'Full Insurance'), ('third', 'Third Party')], copy=True, store=True)
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
    name = fields.Char(string='Reference', copy=True, required=True, readonly=True, store=True)
    need_invoiced = fields.Boolean(string='Need Invoiced', readonly=True)
    note = fields.Html(string='Terms and conditions', copy=True, store=True)
    number = fields.Char(string='Insurance Number', copy=True, required=True, readonly=True, store=True)
    owned_by = fields.Selection(string='Owned By', selection=[('diplomat', 'Diplomat'), ('vendor', 'Vendor')], copy=True, store=True)
    partner_id = fields.Many2one(comodel_name='res.partner', string='Insurance Company', copy=True, required=True, readonly=True, ondelete='restrict', store=True)
    po_count = fields.Integer(string='PO#', readonly=True)
    purchase_order_id = fields.Many2one(comodel_name='purchase.order', string='Purchase Order', copy=True, store=True)
    related_user_ids = fields.Many2many(comodel_name='res.users', string='Notification Users ', copy=True, readonly=True, relation='insurance_policy_res_users_rel', column1='insurance_policy_id', column2='res_users_id', store=True)
    start_date = fields.Date(string='Start Date', copy=True, required=True, readonly=True, store=True)
    state = fields.Selection(string='Status', selection=[('draft', 'Draft'), ('running', 'Running'), ('expired', 'Expired')], 
                                                default='draft', readonly=True, store=True)
    stopped = fields.Boolean(string='Insurance Stopped', readonly=True)
    tax_amount = fields.Float(string='Tax Amount', readonly=True)
    total_amount = fields.Float(string='Total Amount', readonly=True)
    untaxed_amount = fields.Float(string='Untaxed Amount', readonly=True)
    website_message_ids = fields.One2many(comodel_name='mail.message', inverse_name='res_id', string='Website Messages', help="""Website communication history""", store=True)


    _sql_constraints = [
        ('number_uniq', 'unique(number)', 'Insurance Number Must Be Unique!')
    ]
    
    
    def action_confirm(self):
        pass
    
    def action_create_bill(self):
        pass
    
    def action_open_bill(self):
        pass
    
    def action_open_po(self):
        pass
