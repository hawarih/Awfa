from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class RentalContract(models.Model):
    _name = 'rental.contract'
    _description = 'Rental Contract'
    
    
    _inherit = ['mail.thread', 'mail.activity.mixin']
    

    ac = fields.Selection(string='AC Out', selection=[('1', 'Excellent'), ('2', 'Good'), ('3', 'Weak'), ('4', 'Not Working')], copy=True, required=True, store=True)
    ac_in = fields.Selection(string='AC In', selection=[('1', 'Excellent'), ('2', 'Good'), ('3', 'Weak'), ('4', 'Not Working')], copy=True, store=True)
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
    actual_monthly_invoice = fields.Datetime(string='Actual Monthly Invoice', copy=True, store=True)
    additional_service_cost = fields.Float(string='Additional Service Cost', readonly=True)
    additional_services = fields.Many2many(comodel_name='rental.additional.service', string='Additional Services', copy=True, relation='rental_additional_service_rental_contract_rel', column1='rental_contract_id', column2='rental_additional_service_id', store=True)
    another_fuel_out = fields.Selection(string='Fuel Out', selection=[('0', '0'), ('0.25', '0.25'), ('0.5', '0.5'), ('0.75', '0.75'), ('1', '1')], default='0',readonly=True)
    apply_penalty_done = fields.Boolean(string='Apply Penalty Done', copy=True, store=True)
    auth_type = fields.Selection(string='Authorization Type', selection=[('internal', 'Internal'), ('external', 'External')], 
                                 default='internal', copy=True, required=True, store=True)
    car_seats = fields.Selection(string='Car Seats Out', selection=[('6', 'Clean'), ('7', 'Dirty')], copy=True, required=True, store=True)
    car_seats_in = fields.Selection(string='Car Seats In', selection=[('6', 'Clean'), ('7', 'Dirty')], copy=True, store=True)
    category_id = fields.Many2one(comodel_name='fleet.vehicle.model.category', string='Category', related='fleet_vehicle_id.category_id', readonly=True)
    charged_late_hours = fields.Float(string='Charged Late Hours', copy=True, store=True)
    current_date = fields.Date(string='Current Date', copy=True, store=True)
    customer_id = fields.Many2one(comodel_name='res.partner', string='Customer', copy=True, required=True, ondelete='restrict')
    discount = fields.Float(string='Discount', copy=True, store=True)
    discount_amount = fields.Float(string='Discount Amount', readonly=True)
    drop_off_branch_id = fields.Many2one(comodel_name='stock.location', string='Drop Off Branch', copy=True, required=True, ondelete='restrict', store=True)
    due_amount = fields.Float(string='Due Amount', readonly=True)
    duration = fields.Integer(string='Duration', copy=True, required=True, store=True)
    extra_driver = fields.Many2one(comodel_name='res.partner', string='Extra Driver', copy=True, store=True)
    filter_due_amount = fields.Float(string='Filter Due Amount', readonly=True, store=True)
    fire_extinguisher = fields.Selection(string='Fire Extinguisher Out', selection=[('8', 'Available'), ('9', 'Not Available')], copy=True, required=True, store=True)
    fire_extinguisher_in = fields.Selection(string='Fire Extinguisher In', selection=[('8', 'Available'), ('9', 'Not Available')], copy=True, store=True)
    first_aid_kit = fields.Selection(string='First Aid Kit Out', selection=[('8', 'Available'), ('9', 'Not Available')], copy=True, required=True, store=True)
    first_aid_kit_in = fields.Selection(string='First Aid Kit In', selection=[('8', 'Available'), ('9', 'Not Available')], copy=True, store=True)
    fleet_model_id = fields.Many2one(comodel_name='fleet.vehicle.model', string='Model', related='fleet_vehicle_id.model_id', readonly=True)
    fleet_vehicle_id = fields.Many2one(comodel_name='fleet.vehicle', string='Vehicle', copy=True, required=True, ondelete='restrict', store=True)
    fuel_cost = fields.Float(string='Fuel cost', copy=True, readonly=True, store=True)
    fuel_in = fields.Selection(string='Fuel In', selection=[], related='fleet_vehicle_id.current_fuel', readonly=True)
    fuel_out = fields.Selection(string='Fuel Out', selection=[('0', '0'), ('0.25', '0.25'), ('0.5', '0.5'), ('0.75', '0.75'), ('1', '1')], copy=True, store=True)
    fuel_price = fields.Float(string='Fuel Price', copy=True, readonly=True, store=True)
    has_allow_discount_group = fields.Boolean(string='Has Allow Discount Group', readonly=True)
    has_message = fields.Boolean(string='Has Message', readonly=True)
    image1 = fields.Binary(string='Image 1', copy=True, store=True)
    image1_in = fields.Binary(string='Image 1', copy=True, store=True)
    image2 = fields.Binary(string='Image 2', copy=True, store=True)
    image2_in = fields.Binary(string='Image 2', copy=True, store=True)
    image3 = fields.Binary(string='Image 3', copy=True, store=True)
    image3_in = fields.Binary(string='Image 3', copy=True, store=True)
    image4 = fields.Binary(string='Image 4', copy=True, store=True)
    image4_in = fields.Binary(string='Image 4', copy=True, store=True)
    image5 = fields.Binary(string='Image 5', copy=True, store=True)
    image5_in = fields.Binary(string='Image 5', copy=True, store=True)
    image6 = fields.Binary(string='Image 6', copy=True, store=True)
    image6_in = fields.Binary(string='Image 6', copy=True, store=True)
    image7 = fields.Binary(string='Image 7', copy=True, store=True)
    image7_in = fields.Binary(string='Image 7', copy=True, store=True)
    image8 = fields.Binary(string='Image 8', copy=True, store=True)
    image8_in = fields.Binary(string='Image 8', copy=True, store=True)
    image_128 = fields.Binary(string='Logo', related='fleet_vehicle_id.image_128', readonly=True)
    invoice_amount_value = fields.Float(string='Invoice Amount Value', readonly=True)
    invoice_ids = fields.Many2many(comodel_name='account.move', string='Invoice', copy=True, relation='account_move_rental_contract_rel', column1='rental_contract_id', column2='account_move_id', store=True)
    is_corrected = fields.Boolean(string='Is Corrected', copy=True, store=True)
    is_created_return_invoice = fields.Boolean(string='Is Created Return Invoice', copy=True, store=True)
    is_extended = fields.Boolean(string='Extended', copy=True, store=True)
    is_late = fields.Boolean(string='Late', copy=True, store=True)
    is_returned = fields.Boolean(string='Returned', copy=True, store=True)
    keys = fields.Selection(string='Keys Out', selection=[('4', 'Working'), ('5', 'Not Working')], copy=True, required=True, store=True)
    keys_in = fields.Selection(string='Keys In', selection=[('4', 'Working'), ('5', 'Not Working')], copy=True, store=True)
    km_extra_cost = fields.Float(string='Km_Extra_Cost', copy=True, readonly=True, store=True)
    km_free = fields.Float(string='Km Free', copy=True, readonly=True, store=True)
    km_in = fields.Float(string='Km In', copy=True, store=True)
    km_out = fields.Float(string='Km Out', copy=True, store=True)
    last_monthly_invoice = fields.Datetime(string='Last Monthly Invoice', copy=True, store=True)
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
    mobile = fields.Char(string='Mobile', related='customer_id.mobile', readonly=True)
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True)
    name = fields.Char(string='Name', copy=True, readonly=True, translate=True, store=True)
    national_identity_number = fields.Char(string='National Identity Number', related='customer_id.national_identity_number', readonly=True)
    need_extra_driver = fields.Selection(string='Do You Need An Extra Driver ?', selection=[('yes', 'Yes'), ('no', 'No')], 
                                         default='no', copy=True, required=True, store=True)
    next_monthly_invoice = fields.Datetime(string='Next Monthly Invoice', copy=True, store=True)
    paid_amount = fields.Float(string='Paid Amount', readonly=True)
    payment_ids = fields.Many2many(comodel_name='account.payment', string='Payment', copy=True, relation='account_payment_rental_contract_rel', column1='rental_contract_id', column2='account_payment_id', store=True)
    pickup_branch_id = fields.Many2one(comodel_name='stock.location', string='Pickup Branch', copy=True, required=True, ondelete='restrict', store=True)
    pickup_date = fields.Datetime(string='Pickup Date', copy=True, required=True, store=True, default=fields.Date.today())
    previous_amount = fields.Float(string='Previous Amount', copy=True, store=True)
    radio_stereo = fields.Selection(string='Radio Stereo Out', selection=[('1', 'Excellent'), ('2', 'Good'), ('3', 'Weak'), ('4', 'Not Working')], copy=True, required=True, store=True)
    radio_stereo_in = fields.Selection(string='Radio Stereo In', selection=[('1', 'Excellent'), ('2', 'Good'), ('3', 'Weak'), ('4', 'Not Working')], copy=True, store=True)
    ran_schedule_action = fields.Boolean(string='Ran Schedule Action', readonly=True)
    rental_invoices_dates_admin = fields.Boolean(string='Rental Invoices Dates Admin', readonly=True)
    rental_order_lines = fields.One2many(comodel_name='rental.contract.lines', inverse_name='contract_id', string='Rental Order Lines', store=True)
    rental_plan_id = fields.Many2one(comodel_name='customer.rental.plan', string='Rental Plan', copy=True, store=True,
                                     default=lambda self: self.env['customer.rental.plan'].search([('name', '=', 'daily')], limit=1).id)
    rental_policy_id = fields.Many2one(comodel_name='customer.rental.policy', string='Rental Policy', 
                                        copy=True, required=True, ondelete='restrict', store=True,
                                        default=lambda self: self.env['customer.rental.policy'].search([('name', '=', 'actual')], limit=1).id)
    rental_pricing = fields.Many2one(comodel_name='customer.rental.pricing', string='Rental Pricing', copy=True, store=True)
    return_date = fields.Datetime(string='Return Date', readonly=True)
    safety_triangle = fields.Selection(string='Safety Triangle Out', selection=[('8', 'Available'), ('9', 'Not Available')], copy=True, required=True, store=True)
    safety_triangle_in = fields.Selection(string='Safety Triangle In', selection=[('8', 'Available'), ('9', 'Not Available')], copy=True, store=True)
    screen = fields.Selection(string='Screen Out', selection=[('1', 'Excellent'), ('2', 'Good'), ('3', 'Weak'), ('4', 'Not Working')], copy=True, required=True, store=True)
    screen_in = fields.Selection(string='Screen In', selection=[('1', 'Excellent'), ('2', 'Good'), ('3', 'Weak'), ('4', 'Not Working')], copy=True, store=True)
    source = fields.Selection(string='Source', selection=[('branch', 'Branch'), ('website', 'Website')], 
                              default='branch', copy=True, required=True, store=True)
    spare_tire_tools = fields.Selection(string='Spare Tire Tools Out', selection=[('8', 'Available'), ('9', 'Not Available')], copy=True, required=True, store=True)
    spare_tire_tools_in = fields.Selection(string='Spare Tire Tools In', selection=[('8', 'Available'), ('9', 'Not Available')], copy=True, store=True)
    spare_tires = fields.Selection(string='Spare Tires Out', selection=[('1', 'Excellent'), ('2', 'Good'), ('3', 'Weak')], copy=True, required=True, store=True)
    spare_tires_in = fields.Selection(string='Spare Tires In', selection=[('1', 'Excellent'), ('2', 'Good'), ('3', 'Weak')], copy=True, store=True)
    speedometer = fields.Selection(string='Speedometer Out', selection=[('4', 'Working'), ('5', 'Not Working')], copy=True, required=True, store=True)
    speedometer_in = fields.Selection(string='Speedometer In', selection=[('4', 'Working'), ('5', 'Not Working')], copy=True, store=True)
    state = fields.Selection(string='Status', selection=[('draft', 'Draft'), ('open', 'Open'), ('hold', 'Delivered Pending'), 
                                                         ('delivered_indebet', 'Delivered Indebet'), ('closed', 'Closed'), 
                                                         ('cancelled', 'Cancelled')], 
                                                default='draft', store=True)
    tires = fields.Selection(string='Tires Out', selection=[('1', 'Excellent'), ('2', 'Good'), ('3', 'Weak')], copy=True, required=True, store=True)
    tires_in = fields.Selection(string='Tires In', selection=[('1', 'Excellent'), ('2', 'Good'), ('3', 'Weak')], copy=True, store=True)
    total_amount = fields.Float(string='Total Amount', readonly=True)
    total_consumed_fuel = fields.Float(string='Total Consumed Fuel', copy=True, readonly=True, store=True)
    total_dist = fields.Float(string='Total Distance', copy=True, readonly=True, store=True)
    total_km_extra = fields.Float(string='Total Km Extra', copy=True, readonly=True, store=True)
    total_km_extra_cost = fields.Float(string='Total Km Extra Cost', copy=True, readonly=True, store=True)
    total_km_free = fields.Float(string='Total KM Free', copy=True, readonly=True, store=True)
    total_per_day = fields.Float(string='Total Per Day', readonly=True)
    vehicle_cost = fields.Float(string='Vehicle Cost', copy=True, store=True)
    vehicle_status = fields.Selection(string='Vehicle Status Out', selection=[('1', 'Excellent'), ('2', 'Good'), ('3', 'Simple Scratch'), ('4', 'Deep Scratch'), ('5', 'Very Deep Scratch'), ('6', 'Bend In Structure')], copy=True, required=True, store=True)
    vehicle_status_in = fields.Selection(string='Vehicle Status In', selection=[('1', 'Excellent'), ('2', 'Good'), ('3', 'Simple Scratch'), ('4', 'Deep Scratch'), ('5', 'Very Deep Scratch'), ('6', 'Bend In Structure')], copy=True, store=True)
    website_message_ids = fields.One2many(comodel_name='mail.message', inverse_name='res_id', string='Website Messages', help="""Website communication history""", store=True)
    x_studio_datetime_field_OeV9p = fields.Datetime(string='New التاريخ والوقت', copy=True, domain=[], store=True)

    def return_vehicle(self):
        pass
    
    def delay_penalty(self):
        pass
    
    def view_invoices(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Invoices',
            'res_model': 'account.move',
            'view_mode': 'tree,form',  # Opens the tree view, allows switching to form view
            'domain': [('rental_contract_id', '=', self.id)],
            'target': 'current',
        }
    
    def view_accidents(self):
        if not self.env['vehicle.accident'].search([('rental_contract_ids', 'in', [self.id])], limit=1):
            raise ValidationError(_("Please create an accident"))
        else:
            return {
                'type': 'ir.actions.act_window',
                'name': 'Accidents',
                'res_model': 'vehicle.accident',
                'view_mode': 'tree,form',  # Opens the tree view, allows switching to form view
                'domain': [('rental_contract_id', '=', self.id)],
                'target': 'current',
            }
    
    def view_payments(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Payments',
            'res_model': 'account.payment',
            'view_mode': 'tree,form',  # Opens the tree view, allows switching to form view
            'domain': [('rental_contract_id', '=', self.id)],
            'target': 'current',
        }
        
    def _check_customer_has_non_closed_contract(self, customer):
        customer_id = customer
        if customer_id:
            has_non_closed_contract = self.search([('customer_id', '=', customer_id), ('state', 'not in', ['closed', 'cancelled'])], limit=1)
            if has_non_closed_contract:
                raise ValidationError(_('This Customer already has a non closed contract'))
        
    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('rental.contract') or 'New'
        if vals.get('customer_id'):
            self._check_customer_has_non_closed_contract(vals['customer_id'])
        if vals.get('duration') <= 0:
            raise ValidationError('Duration must be bigger than 0')
        
        return super(RentalContract, self).create(vals)
    
    def write(self, vals):
        res = super().write(vals)
        if vals.get('customer_id'):
            self._check_customer_has_non_closed_contract(vals['customer_id'])
        duration = vals.get('duration')
        if duration == 0:
            raise ValidationError('Duration must be bigger than 0')
        if duration and duration <= 0:
            raise ValidationError('Duration must be bigger than 0')
            
        return res
    
    @api.onchange('fleet_vehicle_id')
    def _onchange_fleet_vehicle_id(self):
        if self.fleet_vehicle_id:
            has_rental_pricing = self.env['customer.rental.pricing'].search([('models', 'in', [self.fleet_vehicle_id.model_id.id]), ('state', '=', 'confirmed')], limit=1)
            if not has_rental_pricing:
                raise ValidationError("This vehicle model does not have an active rental pricing")
            self.ac = self.fleet_vehicle_id.ac
            self.car_seats = self.fleet_vehicle_id.car_seats
            self.fire_extinguisher = self.fleet_vehicle_id.fire_extinguisher
            self.first_aid_kit = self.fleet_vehicle_id.first_aid_kit
            self.radio_stereo = self.fleet_vehicle_id.radio_stereo
            self.safety_triangle = self.fleet_vehicle_id.safety_triangle
            self.screen = self.fleet_vehicle_id.screen
            self.spare_tire_tools = self.fleet_vehicle_id.spare_tire_tools
            self.spare_tires = self.fleet_vehicle_id.spare_tires
            self.speedometer = self.fleet_vehicle_id.speedometer
            self.tires = self.fleet_vehicle_id.tires
            self.keys = self.fleet_vehicle_id.keys
            self.vehicle_status = self.fleet_vehicle_id.vehicle_status
            self.km_out = self.fleet_vehicle_id.odometer