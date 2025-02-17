from odoo import api, fields, models


class FleetCard(models.Model):
    _name = 'fleet.card'
    _description = 'Fleet Card'
    
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    activity_calendar_event_id = fields.Many2one(comodel_name='calendar.event', string='Next Activity Calendar Event', readonly=True, ondelete='set null')
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
    assign_gps = fields.Many2one(comodel_name='gps.gps', string='Assign GPS', copy=True, ondelete='set null', store=True, )
    current_location_id = fields.Many2one(comodel_name='stock.location', string='Current Location', readonly=True, ondelete='set null')
    gps_id = fields.Many2one(comodel_name='gps.gps', string='Gps', copy=True, ondelete='set null', store=True)
    gps_state = fields.Selection(string='State', selection=[], related='assign_gps.state', readonly=True, )
    has_message = fields.Boolean(string='Has Message', readonly=True)
    location_id = fields.Many2one(comodel_name='stock.location', string='Location', copy=True, ondelete='set null', store=True, )
    lot_id = fields.Many2one(comodel_name='stock.lot', string='Serial number', copy=True, required=True, ondelete='restrict', store=True, )
    lot_ids = fields.Many2many(comodel_name='stock.lot', string='Lot', readonly=True)
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True)
    message_follower_ids = fields.One2many(comodel_name='mail.followers', inverse_name='res_id', string='Followers', store=True)
    message_has_error = fields.Boolean(string='Message Delivery error', help="""If checked, some messages have a delivery error.""", readonly=True)
    message_has_error_counter = fields.Integer(string='Number of errors', help="""Number of messages with delivery error""", readonly=True)
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', help="""If checked, some messages have a delivery error.""", readonly=True)
    message_ids = fields.One2many(comodel_name='mail.message', inverse_name='res_id', string='Messages', store=True)
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True)
    message_main_attachment_id = fields.Many2one(comodel_name='ir.attachment', string='Main Attachment', ondelete='set null', store=True)
    message_needaction = fields.Boolean(string='Action Needed', help="""If checked, new messages require your attention.""", readonly=True)
    message_needaction_counter = fields.Integer(string='Number of Actions', help="""Number of messages requiring action""", readonly=True)
    message_partner_ids = fields.Many2many(comodel_name='res.partner', string='Followers (Partners)')
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True)
    name = fields.Char(string='Name', copy=True, readonly=True, store=True, )
    related_product = fields.Many2one(comodel_name='product.template', string='Related Product', copy=True, required=True, ondelete='restrict', store=True, )
    scrap_ids = fields.One2many(comodel_name='stock.scrap', inverse_name='card_id', string='Scrap', store=True, )
    state = fields.Selection(string='State', selection=[('draft', 'Draft'), ('working', 'Working'), ('not working', 'Not Working'), ('lost', 'Lost')], 
                                            default='draft', store=True, )
    vehicle_id = fields.Many2one(comodel_name='fleet.vehicle', string='Assign Vehicle', related='assign_gps.assign_vehicle', readonly=True, )
    website_message_ids = fields.One2many(comodel_name='mail.message', inverse_name='res_id', string='Website Messages', help="""Website communication history""", store=True)


    def action_confirm(self):
        pass

    def action_confirm(self):
        pass

    def action_reset_to_draft(self):
        pass

    def action_clear(self):
        pass

    def action_scrap_card(self):
        pass

    def action_view_scrap_ids(self):
        pass
