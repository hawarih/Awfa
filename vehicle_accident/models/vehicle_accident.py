from odoo import api, fields, models
from odoo.exceptions import UserError


class VehicleAccident(models.Model):
    _name = 'vehicle.accident'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'analytic.mixin']

    _description = 'Vehicle Accident'

    accident_date = fields.Date(string='Accident Date', copy=True, store=True)
    accident_journal_id = fields.Many2one(comodel_name='account.journal', string='Journals', related='company_id.accident_journal_id', readonly=True)
    accident_policy = fields.Float(string='Accident Policy', copy=True, readonly=True, store=True)
    accident_type = fields.Selection(string='Accident Type', selection=[('first', 'First'), ('shared', 'Shared'), ('accident_without_contract', 'Accident Without Contract')], copy=True, store=True)
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
    announcement_date = fields.Date(string='Announcement Date', copy=True, store=True)
    city = fields.Many2one(comodel_name='res.country.state', string='City', copy=True, store=True)
    comment = fields.Text(string='Comment', copy=True, store=True)
    company_id = fields.Many2one(comodel_name='res.company', string='Company', copy=True, store=True)
    customer_accident_percentage = fields.Float(string='customer Accident Percentage', copy=True, store=True)
    customer_id = fields.Many2one(comodel_name='res.partner', string='Customer', copy=True, store=True)
    deductible_amount = fields.Float(string='Deductible Amount', related='accident_policy', readonly=True)
    document_state = fields.Selection(string='Document State', selection=[('valid', 'Valid'), ('not_vaild', 'Not Valid')], readonly=True)
    estimation_attachment = fields.Binary(string='Estimation Attachment', copy=True, store=True)
    evaluation_party = fields.Many2one(comodel_name='evaluation.party', string='Evaluation Party', copy=True, store=True)
    evaluation_type = fields.Selection(string='Evaluation Type', selection=[('external', 'External'), ('deductible', 'Deductible')], copy=True, store=True)
    external_hand_wages = fields.Float(string='Hand Wages', copy=True, store=True)
    external_spare_parts = fields.Float(string='Spare Parts', copy=True, store=True)
    first_side_id = fields.Many2one(comodel_name='product.product', string='First Side', related='company_id.first_side_id', readonly=True)
    follower_id = fields.Many2one(comodel_name='hr.employee', string='Follower', copy=True, store=True)
    has_message = fields.Boolean(string='Has Message', readonly=True)
    insurance_id = fields.Many2one(comodel_name='insurance.policy', string='Insurance', copy=True, store=True)
    insurance_type = fields.Selection(string='Insurance Type', selection=[('full', 'Full Insurance'), ('third', 'Third Party')], copy=True, readonly=True, store=True)
    invoice_ids = fields.Many2many(comodel_name='account.move', string='Invoice', copy=True, relation='account_move_vehicle_accident_rel', column1='vehicle_accident_id', column2='account_move_id', store=True)
    is_external = fields.Boolean(string='Is External', copy=True, store=True)
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
    name = fields.Char(string='Name', copy=True, readonly=True, translate=True, store=True)
    national_identity_number = fields.Char(string='National Identity Number', related='customer_id.national_identity_number', readonly=True)
    not_insurance_reasons = fields.Many2one(comodel_name='not.insurance.reason', string='Not Insurance Reasons', copy=True, store=True)
    other_party_accident_percentage = fields.Float(string='Other Party Accident Percentage', copy=True, store=True)
    other_party_id = fields.Many2one(comodel_name='res.partner', string='Other Party', copy=True, store=True)
    rental_contract_ids = fields.Many2one(comodel_name='rental.contract', string='Rental Contract', copy=True, store=True)
    report_accident_number = fields.Text(string='Report Accident Number', copy=True, store=True)
    report_attachment = fields.Binary(string='Report Attachment', copy=True, store=True)
    report_date = fields.Date(string='Report Date', copy=True, store=True)
    report_source = fields.Selection(string='Report Source', selection=[('nagm', 'Nagm'), ('morror', 'Morror')], copy=True, store=True)
    second_side_id = fields.Many2one(comodel_name='product.product', string='Second Side', related='company_id.second_side_id', readonly=True)
    shared_customer_accident_percentage = fields.Selection(string='Customer Percentage', selection=[('0', '0 %'), ('25', '25 %'), ('50', '50 %'), ('75', '75 %'), ('100', '100 %')], copy=True, store=True)
    shared_other_party_accident_percentage = fields.Selection(string='Other Party Percentage', selection=[('0', '0 %'), ('25', '25 %'), ('50', '50 %'), ('75', '75 %'), ('100', '100 %')], copy=True, store=True)
    state = fields.Selection(string='State', selection=[('announcement', 'Announcement'), ('reporting', 'Reporting'), 
                                                        ('evaluation', 'Evaluation'), ('waiting_insurance_document', 'Waiting Insurance Document'), 
                                                        ('due_amount', 'Due Amount'), ('closed', 'Closed'), ('cancel', 'Canceled')], 
                                                default='announcement', store=True)
    third_side_id = fields.Many2one(comodel_name='product.product', string='Third Side', related='company_id.third_side_id', readonly=True)
    total_external_evaluation = fields.Float(string='Total External Evaluation', readonly=True)
    vehicle = fields.Many2one(comodel_name='fleet.vehicle', string='Vehicle', copy=True, store=True)
    vehicle_lines_ids = fields.One2many(comodel_name='vehicle.accident.lines', inverse_name='vehicle_accident_id', string='Lines', store=True)
    website_message_ids = fields.One2many(comodel_name='mail.message', inverse_name='res_id', string='Website Messages', help="""Website communication history""", store=True)

    def action_previous(self):
        if self.state == 'waiting_insurance_document':
            self.state = 'evaluation'
        elif self.state == 'waiting_insurance_document':
            self.state = 'evaluation'
        else:
            self.state = 'announcement'

    def action_next(self):
        self.state = 'reporting'

    def action_next2(self):
        self.state = 'evaluation'

    def action_next3(self):
        self.state = 'waiting_insurance_document'

    def action_lines_amount_computation(self):
        self.state = 'due_amount'

    def action_close(self):
        self.state = 'closed'

    def action_cancel(self):
        self.state = 'cancel'

    def view_invoices(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Invoices',
            'res_model': 'account.move',
            'view_mode': 'tree,form',  # Opens the tree view, allows switching to form view
            'target': 'current',
        }

    def confirm_button(self):
        pass

    @api.onchange('vehicle')
    def _onchange_vehicle(self):
        for record in self:
            vehicle_insu_type = record.vehicle.insurance_type
            if vehicle_insu_type:
                record.insurance_type = vehicle_insu_type

    @api.model_create_multi
    def create(self, vals_list):
        for val in vals_list:
            if val.get('name', 'New') == 'New':
                val['name'] = self.env['ir.sequence'].next_by_code('vehicle.accident') or 'New'
                val['document_state'] = 'valid'
        return super().create(vals_list)
