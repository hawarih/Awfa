from odoo import api, fields, models


class MaterialPurchaseRequisition(models.Model):
    _name = 'material.purchase.requisition'
    _description = 'Material Purchase Requisition'

    access_token = fields.Char(string='Security Token', store=True)
    access_url = fields.Char(string='Portal Access URL', help="""Customer Portal URL""", readonly=True)
    access_warning = fields.Text(string='Access warning', readonly=True)
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
    approve_employee_id = fields.Many2one(comodel_name='hr.employee', string='Approved by', readonly=True, store=True)
    company_id = fields.Many2one(comodel_name='res.company', string='Company', copy=True, required=True, ondelete='restrict', store=True)
    custom_picking_type_id = fields.Many2one(comodel_name='stock.picking.type', string='Picking Type', store=True)
    date_confirm = fields.Date(string='Confirmed Date', readonly=True, store=True)
    date_done = fields.Date(string='Date Done', help="""Date of Completion of Purchase Requisition""", copy=True, readonly=True, store=True)
    date_end = fields.Date(string='Requisition Deadline', help="""Last date for the product to be needed""", copy=True, readonly=True, store=True)
    date_receive = fields.Date(string='Received Date', readonly=True, store=True)
    date_request = fields.Date(string='Requisition Date', copy=True, required=True, store=True)
    date_user_approved = fields.Date(string='Approved Date', readonly=True, store=True)
    date_user_reject = fields.Date(string='Rejected Date', readonly=True, store=True)
    delivery_picking_id = fields.Many2one(comodel_name='stock.picking', string='Internal Picking', readonly=True, store=True)
    dest_location_id = fields.Many2one(comodel_name='stock.location', string='Destination Location', help="""Location where the system will stock the finished products.""", copy=True, store=True)
    employee_confirm_id = fields.Many2one(comodel_name='hr.employee', string='Confirmed by', readonly=True, store=True)
    employee_id = fields.Many2one(comodel_name='hr.employee', string='Employee', copy=True, required=True, ondelete='restrict', store=True)
    has_message = fields.Boolean(string='Has Message', readonly=True)
    internal_picking_count = fields.Integer(string='Internal Picking', readonly=True)
    location_id = fields.Many2one(comodel_name='stock.location', string='Source Location', copy=True, store=True)
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
    name = fields.Char(string='Number', copy=True, readonly=True, index=True, store=True)
    note = fields.Text(string='Reason for Requisitions', copy=True, store=True)
    purchase_order_count = fields.Integer(string='Purchase Order', readonly=True)
    purchase_order_ids = fields.One2many(comodel_name='purchase.order', inverse_name='custom_requisition_id', string='Purchase Ordes', store=True)
    reject_employee_id = fields.Many2one(comodel_name='hr.employee', string='Rejected by', readonly=True, store=True)
    requisition_line_ids = fields.One2many(comodel_name='material.purchase.requisition.line', inverse_name='requisition_id', string='Purchase Requisitions Line', copy=True, store=True)
    requisition_responsible_id = fields.Many2one(comodel_name='hr.employee', string='Requisition Responsible', copy=True, store=True)
    state = fields.Selection(string='State', selection=[('draft', 'New'), ('ir_approve', 'Waiting IR Approved'), 
                                                        ('approve', 'Approved'), ('stock', 'Purchase Order Created'), 
                                                        ('receive', 'Received'), ('cancel', 'Cancelled'), ('reject', 'Rejected')], 
                                                default='draft', store=True)
    website_message_ids = fields.One2many(comodel_name='mail.message', inverse_name='res_id', string='Website Messages', help="""Website communication history""", store=True)

    def manager_approve(self):
        pass
    
    def user_approve(self):
        pass
    
    def request_stock(self):
        pass
    
    def action_received(self):
        pass
    
    def requisition_reject(self):
        pass
    
    def action_cancel(self):
        pass
    
    def reset_draft(self):
        pass
    
    def action_view_stock_picking(self):
        pass
    
    def action_view_purchase_order(self):
        pass