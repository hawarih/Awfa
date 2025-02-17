from odoo import api, fields, models
from odoo.exceptions import UserError


class VehicleDamage(models.Model):
    _name = 'vehicle.damage'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'analytic.mixin']
    
    _description = 'Vehicle Damage'

    ac = fields.Selection(string='AC In', selection=[('1', 'Excellent'), ('2', 'Good'), ('3', 'Weak'), ('4', 'Not Working')], copy=True, store=True)
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
    car_seats = fields.Selection(string='Car Seats In', selection=[('6', 'Clean'), ('7', 'Dirty')], copy=True, store=True)
    category_id = fields.Many2one(comodel_name='fleet.vehicle.model.category', string='Category', related='fleet_vehicle_id.category_id', readonly=True)
    customer = fields.Many2one(comodel_name='res.partner', string='Customer', related='rental_contract.customer_id', readonly=True)
    evaluation_party = fields.Many2one(comodel_name='evaluation.party', string='Evaluation Party', copy=True, store=True)
    fire_extinguisher = fields.Selection(string='Fire Extinguisher In', selection=[('8', 'Available'), ('9', 'Not Available')], copy=True, store=True)
    first_aid_kit = fields.Selection(string='First Aid Kit IN', selection=[('8', 'Available'), ('9', 'Not Available')], copy=True, store=True)
    fleet_model_id = fields.Many2one(comodel_name='fleet.vehicle.model', string='Model', related='fleet_vehicle_id.model_id', readonly=True)
    fleet_vehicle_id = fields.Many2one(comodel_name='fleet.vehicle', string='Vehicle', copy=True, store=True)
    fuel_in = fields.Selection(string='Fuel IN', selection=[('0', '0'), ('0.25', '0.25'), ('0.5', '0.5'), ('0.75', '0.75'), ('1', '1')], copy=True, store=True)
    has_message = fields.Boolean(string='Has Message', readonly=True)
    image1 = fields.Binary(string='Image 1', copy=True, store=True)
    image2 = fields.Binary(string='Image 2', copy=True, store=True)
    image3 = fields.Binary(string='Image 3', copy=True, store=True)
    image4 = fields.Binary(string='Image 4', copy=True, store=True)
    image5 = fields.Binary(string='Image 5', copy=True, store=True)
    image6 = fields.Binary(string='Image 6', copy=True, store=True)
    image7 = fields.Binary(string='Image 7', copy=True, store=True)
    image8 = fields.Binary(string='Image 8', copy=True, store=True)
    keys = fields.Selection(string='Keys In', selection=[('4', 'Working'), ('5', 'Not Working')], copy=True, store=True)
    km_in = fields.Float(string='Km IN', copy=True, store=True)
    licence_plate = fields.Char(string='License Plate', help="""License plate number of the vehicle (i = plate number for a car)""", related='fleet_vehicle_id.license_plate', readonly=True)
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
    radio_stereo = fields.Selection(string='Radio Stereo In', selection=[('1', 'Excellent'), ('2', 'Good'), ('3', 'Weak'), ('4', 'Not Working')], copy=True, store=True)
    rental_contract = fields.Many2one(comodel_name='rental.contract', string='Rental Contract', copy=True, store=True)
    safety_triangle = fields.Selection(string='Safety Triangle In', selection=[('8', 'Available'), ('9', 'Not Available')], copy=True, store=True)
    screen = fields.Selection(string='Screen In', selection=[('1', 'Excellent'), ('2', 'Good'), ('3', 'Weak'), ('4', 'Not Working')], copy=True, store=True)
    spare_tire_tools = fields.Selection(string='Spare Tire Tools IN', selection=[('8', 'Available'), ('9', 'Not Available')], copy=True, store=True)
    spare_tires = fields.Selection(string='Spare Tires IN', selection=[('1', 'Excellent'), ('2', 'Good'), ('3', 'Weak')], copy=True, store=True)
    speedometer = fields.Selection(string='Speedometer In', selection=[('4', 'Working'), ('5', 'Not Working')], copy=True, store=True)
    state = fields.Selection(string='State', selection=[('waiting', 'Waiting Damage Evaluation'), ('evaluated', 'Evaluated'), ('cancel', 'cancelled')],
                             default='waiting', store=True)
    tax = fields.Many2many(comodel_name='account.tax', string='Tax', readonly=True)
    tires = fields.Selection(string='Tires IN', selection=[('1', 'Excellent'), ('2', 'Good'), ('3', 'Weak')], copy=True, store=True)
    total_with_tax = fields.Float(string='Total With Tax', readonly=True)
    total_without_tax = fields.Float(string='Total Without Tax', compute='_compute_total_without_tax')
    vehicle_damage_lines = fields.One2many(comodel_name='vehicle.damage.lines', inverse_name='vehicle_damage_id', string='Vehicle Damage Lines', store=True)
    vehicle_status = fields.Selection(string='Vehicle Status Out', selection=[('1', 'Excellent'), ('2', 'Good'), ('3', 'Simple Scratch'), ('4', 'Deep Scratch'), ('5', 'Very Deep Scratch'), ('6', 'Bend In Structure')], copy=True, store=True)
    website_message_ids = fields.One2many(comodel_name='mail.message', inverse_name='res_id', string='Website Messages', help="""Website communication history""", store=True)

    def confirm(self):
        pass

    def cancel(self):
        pass

    @api.model_create_multi
    def create(self, vals_list):
        for val in vals_list:
            val['tax'] = self.env['account.tax'].search([('name', '=', 'Sales tax'), ('active', '=', True)]).ids
        return super().create(vals_list)

    def _compute_total_without_tax(self):
        for record in self:
            total = sum(line.amount for line in record.vehicle_damage_lines)
            record.total_without_tax = total