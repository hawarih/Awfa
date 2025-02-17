from odoo import api, fields, models


class VehicleTermination(models.Model):
    _name = 'vehicle.termination'
    _description = 'Vehicle Termination'
    
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
    asset_count = fields.Integer(string='Asset Count', readonly=True)
    asset_line_ids = fields.One2many(comodel_name='termination.asset.line', inverse_name='termination_id', string='Asset Line', store=True)
    company_id = fields.Many2one(comodel_name='res.company', string='Company', copy=True, required=True, readonly=True, ondelete='restrict', store=True)
    credit_note_count = fields.Integer(string='Credit Note Count', readonly=True)
    date = fields.Date(string='Date', copy=True, store=True)
    expense_count = fields.Integer(string='Expense Count', readonly=True)
    expense_line_ids = fields.One2many(comodel_name='termination.expense.line', inverse_name='termination_id', string='Expense Line', store=True)
    has_message = fields.Boolean(string='Has Message', readonly=True)
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True)
    message_follower_ids = fields.One2many(comodel_name='mail.followers', inverse_name='res_id', string='Followers', store=True)
    message_has_error = fields.Boolean(string='Message Delivery error', help="""If checked, some messages have a delivery error.""", readonly=True)
    message_has_error_counter = fields.Integer(string='Number of errors', help="""Number of messages with delivery error""", readonly=True)
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', help="""If checked, some messages have a delivery error.""", readonly=True)
    message_ids = fields.One2many(comodel_name='mail.message', inverse_name='res_id', string='Messages', store=True)
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True)
    message_main_attachment_id = fields.Many2one(comodel_name='ir.attachment', string='Main Attachment',  store=True)
    message_needaction = fields.Boolean(string='Action Needed', help="""If checked, new messages require your attention.""", readonly=True)
    message_needaction_counter = fields.Integer(string='Number of Actions', help="""Number of messages requiring action""", readonly=True)
    message_partner_ids = fields.Many2many(comodel_name='res.partner', string='Followers (Partners)')
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True)
    product_ids = fields.Many2many(comodel_name='product.template', string='Product', copy=True, relation='product_template_vehicle_termination_rel', column1='vehicle_termination_id', column2='product_template_id', store=True)
    request_number = fields.Char(string='Request Number', readonly=True, store=True)
    state = fields.Selection(string='State', selection=[('draft', 'Draft'), ('confirm', 'Posted')], store=True, default='draft')
    termination_type = fields.Selection(string='Termination Type', selection=[('sell', 'Sell'), ('total_damage', 'Total Damage'), ('transfer', 'Transfer')], copy=True, store=True)
    website_message_ids = fields.One2many(comodel_name='mail.message', inverse_name='res_id', string='Website Messages', help="""Website communication history""", store=True)

    def generate(self):
        pass

    def confirm(self):
        pass

    def reset(self):
        pass

    def action_view_related_assets(self):
        pass

    def action_view_related_expense(self):
        pass

    def action_view_credit_note(self):
        pass
