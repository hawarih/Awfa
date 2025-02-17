from odoo import api, fields, models


class VehiclePreventiveMaintenance(models.Model):
    _name = 'vehicle.preventive.maintenance'
    _description = 'Vehicle Preventive Maintenance'
    
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    Last_maintenance_request_id = fields.Many2one(comodel_name='maintenance.request', string='Last Maintenance Request', copy=True,  store=True)
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
    has_message = fields.Boolean(string='Has Message', readonly=True)
    last_maintenance_date = fields.Date(string='Last Maintenance Date', copy=True, store=True)
    last_maintenance_odometer = fields.Float(string='Last Maintenance Odometer', copy=True, store=True)
    maintenance_plan_id = fields.Many2one(comodel_name='preventive.maintenance.plan', string='Maintenance Plan', copy=True,  store=True)
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
    need_maintenance_every_km = fields.Integer(string='Kilometer', related='maintenance_plan_id.kilometer', readonly=True)
    need_maintenance_every_month = fields.Integer(string='Months', related='maintenance_plan_id.months', readonly=True)
    next_maintenance_date = fields.Date(string='Next Maintenance Date', readonly=True)
    next_maintenance_odometer = fields.Float(string='Next Maintenance Odometer', readonly=True)
    remaining = fields.Float(string='Remaining', readonly=True)
    remaining_notification_sent = fields.Boolean(string='Remaining Notification Sent', copy=True, store=True)
    vehicle_id = fields.Many2one(comodel_name='fleet.vehicle', string='Vehicle', copy=True,  store=True)
    vehicle_last_odometer = fields.Float(string='Last Odometer', help="""Odometer measure of the vehicle at the moment of this log""", related='vehicle_id.odometer', readonly=True)
    website_message_ids = fields.One2many(comodel_name='mail.message', inverse_name='res_id', string='Website Messages', help="""Website communication history""", store=True)
