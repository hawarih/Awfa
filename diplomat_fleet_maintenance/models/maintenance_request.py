from odoo import api, fields, models


class MaintenanceRequest(models.Model):
    _inherit = 'maintenance.request'

    ac_in = fields.Selection(string='Ac In', selection=[('1', 'Excellent'), ('2', 'Good'), ('3', 'Week'), ('4', 'Not Working')], copy=True, store=True)
    ac_in2 = fields.Selection(string='Ac In', selection=[], related='ac_in', readonly=True)
    ac_out = fields.Selection(string='Ac Out', selection=[('1', 'Excellent'), ('2', 'Good'), ('3', 'Week'), ('4', 'Not Working')], copy=True, store=True)
    ac_out2 = fields.Selection(string='Ac Out', selection=[], related='ac_out', readonly=True)
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
    amount = fields.Float(string='Amount', copy=True, store=True)
    bill_count = fields.Integer(string='Bill Count', readonly=True)
    bill_ids = fields.One2many(comodel_name='account.move', inverse_name='maintenance_id', string='Bill', store=True)
    car_seats_in = fields.Selection(string='Car Seats In', selection=[('6', 'Clean'), ('7', 'Dirty')], copy=True, store=True)
    car_seats_in2 = fields.Selection(string='Car Seats In', selection=[], related='car_seats_in', readonly=True)
    car_seats_out = fields.Selection(string='Car Seats Out', selection=[('6', 'Clean'), ('7', 'Dirty')], copy=True, store=True)
    car_seats_out2 = fields.Selection(string='Car Seats Out', selection=[], related='car_seats_out', readonly=True)
    currency_id = fields.Many2one(comodel_name='res.currency', string='Currency', readonly=True,  store=True)
    entry_attachment = fields.Many2many(comodel_name='ir.attachment', string='Entry Attachment', copy=True, relation='maintenance_request_entry_attachment', column1='maintenance_request_id', column2='ir_attachment_id', store=True)
    entry_description = fields.Text(string='Entry Description', copy=True, store=True)
    fire_extinguisher_in = fields.Selection(string='Fire Extinguisher In', selection=[('8', 'Available'), ('9', 'Not Available')], copy=True, store=True)
    fire_extinguisher_in2 = fields.Selection(string='Fire Extinguisher In', selection=[], related='fire_extinguisher_in', readonly=True)
    fire_extinguisher_out = fields.Selection(string='Fire Extinguisher Out', selection=[('8', 'Available'), ('9', 'Not Available')], copy=True, store=True)
    fire_extinguisher_out2 = fields.Selection(string='Fire Extinguisher Out', selection=[], related='fire_extinguisher_out', readonly=True)
    first_aid_kit_in = fields.Selection(string='First Aid Kit In', selection=[('8', 'Available'), ('9', 'Not Available')], copy=True, store=True)
    first_aid_kit_in2 = fields.Selection(string='First Aid Kit In', selection=[], related='first_aid_kit_in', readonly=True)
    first_aid_kit_out = fields.Selection(string='First Aid Kit Out', selection=[('8', 'Available'), ('9', 'Not Available')], copy=True, store=True)
    first_aid_kit_out2 = fields.Selection(string='First Aid Kit Out', selection=[], related='first_aid_kit_out', readonly=True)
    fuel_in = fields.Selection(string='Fuel In', selection=[('0', '0'), ('0.25', '0.25'), ('0.5', '0.5'), ('0.75', '0.75'), ('1', '1')], copy=True, store=True)
    fuel_in2 = fields.Selection(string='Fuel In', selection=[], related='fuel_in', readonly=True)
    fuel_out = fields.Selection(string='Fuel Out', selection=[('0', '0'), ('0.25', '0.25'), ('0.5', '0.5'), ('0.75', '0.75'), ('1', '1')], copy=True, store=True)
    fuel_out2 = fields.Selection(string='Fuel Out', selection=[], related='fuel_out', readonly=True)
    has_message = fields.Boolean(string='Has Message', readonly=True)
    image_in_1 = fields.Binary(string='Image 1', copy=True, store=True)
    image_in_12 = fields.Binary(string='Image 1', related='image_in_1', readonly=True)
    image_in_2 = fields.Binary(string='Image 2', copy=True, store=True)
    image_in_22 = fields.Binary(string='Image 2', related='image_in_2', readonly=True)
    image_in_3 = fields.Binary(string='Image 3', copy=True, store=True)
    image_in_32 = fields.Binary(string='Image 3', related='image_in_3', readonly=True)
    image_in_4 = fields.Binary(string='Image 4', copy=True, store=True)
    image_in_42 = fields.Binary(string='Image 4', related='image_in_4', readonly=True)
    image_in_5 = fields.Binary(string='Image 5', copy=True, store=True)
    image_in_52 = fields.Binary(string='Image 5', related='image_in_5', readonly=True)
    image_in_6 = fields.Binary(string='Image 6', copy=True, store=True)
    image_in_62 = fields.Binary(string='Image 6', related='image_in_6', readonly=True)
    image_in_7 = fields.Binary(string='Image 7', copy=True, store=True)
    image_in_72 = fields.Binary(string='Image 7', related='image_in_7', readonly=True)
    image_in_8 = fields.Binary(string='Image 8', copy=True, store=True)
    image_in_82 = fields.Binary(string='Image 8', related='image_in_8', readonly=True)
    image_out_1 = fields.Binary(string='Image 1', copy=True, store=True)
    image_out_12 = fields.Binary(string='Image 1', related='image_out_1', readonly=True)
    image_out_2 = fields.Binary(string='Image 2', copy=True, store=True)
    image_out_22 = fields.Binary(string='Image 2', related='image_out_2', readonly=True)
    image_out_3 = fields.Binary(string='Image 3', copy=True, store=True)
    image_out_32 = fields.Binary(string='Image 3', related='image_out_3', readonly=True)
    image_out_4 = fields.Binary(string='Image 4', copy=True, store=True)
    image_out_42 = fields.Binary(string='Image 4', related='image_out_4', readonly=True)
    image_out_5 = fields.Binary(string='Image 5', copy=True, store=True)
    image_out_52 = fields.Binary(string='Image 5', related='image_out_5', readonly=True)
    image_out_6 = fields.Binary(string='Image 6', copy=True, store=True)
    image_out_62 = fields.Binary(string='Image 6', related='image_out_6', readonly=True)
    image_out_7 = fields.Binary(string='Image 7', copy=True, store=True)
    image_out_72 = fields.Binary(string='Image 7', related='image_out_7', readonly=True)
    image_out_8 = fields.Binary(string='Image 8', copy=True, store=True)
    image_out_82 = fields.Binary(string='Image 8', related='image_out_8', readonly=True)
    keys_in = fields.Selection(string='Keys In', selection=[('4', 'Working'), ('5', 'Not Working')], copy=True, store=True)
    keys_in2 = fields.Selection(string='Keys In', selection=[], related='keys_in', readonly=True)
    keys_out = fields.Selection(string='Keys Out', selection=[('4', 'Working'), ('5', 'Not Working')], copy=True, store=True)
    keys_out2 = fields.Selection(string='Keys Out', selection=[], related='keys_out', readonly=True)
    km_in = fields.Float(string='Km In', readonly=True, store=True)
    km_in2 = fields.Float(string='Km In', related='km_in', readonly=True)
    km_out = fields.Float(string='Km Out', copy=True, store=True)
    km_out2 = fields.Float(string='Km Out', related='km_out', readonly=True)
    license_plate = fields.Char(string='License Plate', help="""License plate number of the vehicle (i = plate number for a car)""", related='vehicle_id.license_plate', readonly=True, tracking=100)
    location_type = fields.Selection(string='Location Type', selection=[('internal', 'Internal'), ('external', 'External'), ('insurance', 'Insurance')], copy=True, store=True)
    maintenance_repair_task_lines = fields.One2many(comodel_name='maintenance.repair.task.line', inverse_name='maintenance_id', string='Maintenance Repair Task Lines', store=True)
    maintenance_spare_part_lines = fields.One2many(comodel_name='maintenance.spare.part.line', inverse_name='maintenance_id', string='Maintenance Spare Part Lines', store=True)
    maintenance_type = fields.Selection(string='Maintenance Type', selection=[('corrective', 'Accident and Damage'), ('preventive', 'Preventive')], copy=True, store=True)
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
    model_id = fields.Many2one(comodel_name='fleet.vehicle.model', string='Model', related='vehicle_id.model_id', readonly=True, tracking=100)
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True)
    out_attachment = fields.Many2many(comodel_name='ir.attachment', string='Out Attachment', copy=True, relation='maintenance_request_out_attachment', column1='maintenance_request_id', column2='ir_attachment_id', store=True)
    out_description = fields.Text(string='Out Description', copy=True, store=True)
    picking_count = fields.Integer(string='Picking Count', readonly=True)
    picking_ids = fields.One2many(comodel_name='stock.picking', inverse_name='maintenance_id', string='Picking', store=True)
    preventive_maintenance_plan_id = fields.Many2one(comodel_name='preventive.maintenance.plan', string='Preventive Maintenance Plan', copy=True,  store=True)
    preventive_maintenance_plan_ids = fields.Many2one(comodel_name='preventive.maintenance.plan', string='Preventive Maintenance Plan', copy=True,  store=True)
    radio_stereo_in = fields.Selection(string='Radio Stereo In', selection=[('1', 'Excellent'), ('2', 'Good'), ('3', 'Week'), ('4', 'Not Working')], copy=True, store=True)
    radio_stereo_in2 = fields.Selection(string='Radio Stereo In', selection=[], related='radio_stereo_in', readonly=True)
    radio_stereo_out = fields.Selection(string='Radio Stereo Out', selection=[('1', 'Excellent'), ('2', 'Good'), ('3', 'Week'), ('4', 'Not Working')], copy=True, store=True)
    radio_stereo_out2 = fields.Selection(string='Radio Stereo Out', selection=[], related='radio_stereo_out', readonly=True)
    repair_close_date = fields.Datetime(string='Repair Close Date', copy=True, store=True)
    repair_duration = fields.Float(string='Repair Duration', readonly=True)
    repair_request_date = fields.Datetime(string='Repair Request Date', copy=True, store=True)
    repair_task_ids = fields.Many2many(comodel_name='repair.task', string='Repair Task', copy=True, relation='maintenance_request_repair_task_rel', column1='maintenance_request_id', column2='repair_task_id', store=True)
    responsible_id = fields.Many2one(comodel_name='hr.employee', string='Responsible', copy=True,  store=True)
    safety_triangle_in = fields.Selection(string='Safety Triangle In', selection=[('8', 'Available'), ('9', 'Not Available')], copy=True, store=True)
    safety_triangle_in2 = fields.Selection(string='Safety Triangle In', selection=[], related='safety_triangle_in', readonly=True)
    safety_triangle_out = fields.Selection(string='Safety Triangle Out', selection=[('8', 'Available'), ('9', 'Not Available')], copy=True, store=True)
    safety_triangle_out2 = fields.Selection(string='Safety Triangle Out', selection=[], related='safety_triangle_out', readonly=True)
    screen_in = fields.Selection(string='Screen In', selection=[('1', 'Excellent'), ('2', 'Good'), ('3', 'Week'), ('4', 'Not Working')], copy=True, store=True)
    screen_in2 = fields.Selection(string='Screen In', selection=[], related='screen_in', readonly=True)
    screen_out = fields.Selection(string='Screen Out', selection=[('1', 'Excellent'), ('2', 'Good'), ('3', 'Week'), ('4', 'Not Working')], copy=True, store=True)
    screen_out2 = fields.Selection(string='Screen Out', selection=[], related='screen_out', readonly=True)
    spare_tire_tools_in = fields.Selection(string='Spare Tire Tools In', selection=[('8', 'Available'), ('9', 'Not Available')], copy=True, store=True)
    spare_tire_tools_in2 = fields.Selection(string='Spare Tire Tools In', selection=[], related='spare_tire_tools_in', readonly=True)
    spare_tire_tools_out = fields.Selection(string='Spare Tire Tools Out', selection=[('8', 'Available'), ('9', 'Not Available')], copy=True, store=True)
    spare_tire_tools_out2 = fields.Selection(string='Spare Tire Tools Out', selection=[], related='spare_tire_tools_out', readonly=True)
    spare_tires_in = fields.Selection(string='Spare Tires In', selection=[('1', 'Excellent'), ('2', 'Good'), ('3', 'Week')], copy=True, store=True)
    spare_tires_in2 = fields.Selection(string='Spare Tires In', selection=[], related='spare_tires_in', readonly=True)
    spare_tires_out = fields.Selection(string='Spare Tires Out', selection=[('1', 'Excellent'), ('2', 'Good'), ('3', 'Week')], copy=True, store=True)
    spare_tires_out2 = fields.Selection(string='Spare Tires Out', selection=[], related='spare_tires_out', readonly=True)
    speedometer_in = fields.Selection(string='Speedometer In', selection=[('4', 'Working'), ('5', 'Not Working')], copy=True, store=True)
    speedometer_in2 = fields.Selection(string='Speedometer In', selection=[], related='speedometer_in', readonly=True)
    speedometer_out = fields.Selection(string='Speedometer Out', selection=[('4', 'Working'), ('5', 'Not Working')], copy=True, store=True)
    speedometer_out2 = fields.Selection(string='Speedometer Out', selection=[], related='speedometer_out', readonly=True)
    stage_cancel = fields.Boolean(string='Cancel', related='stage_id.cancel', readonly=True)
    stage_closed = fields.Boolean(string='Close', related='stage_id.close', readonly=True)
    stage_confirm = fields.Boolean(string='Confirm', related='stage_id.confirm', readonly=True)
    stage_done = fields.Boolean(string='Request Done', related='stage_id.done', readonly=True)
    stage_draft = fields.Boolean(string='Reset To Draft', related='stage_id.reset_to_draft', readonly=True)
    stock_transfer_count = fields.Integer(string='Stock Transfer Count', readonly=True)
    team_location = fields.Many2one(comodel_name='stock.location', string='Team Location', readonly=True)
    tires_in = fields.Selection(string='Tires In', selection=[('1', 'Excellent'), ('2', 'Good'), ('3', 'Week')], copy=True, store=True)
    tires_in2 = fields.Selection(string='Tires In', selection=[], related='tires_in', readonly=True)
    tires_out = fields.Selection(string='Tires Out', selection=[('1', 'Excellent'), ('2', 'Good'), ('3', 'Week')], copy=True, store=True)
    tires_out2 = fields.Selection(string='Tires Out', selection=[], related='tires_out', readonly=True)
    total_maintenance_amount = fields.Monetary(string='Total Maintenance Amount', readonly=True)
    vehicle_id = fields.Many2one(comodel_name='fleet.vehicle', string='Vehicle', copy=True,  store=True)
    vehicle_status_in = fields.Selection(string='Vehicle Status In', selection=[('1', 'Excellent'), ('2', 'Good'), ('3', 'Simple Scratch'), ('4', 'Deep Scratch'), ('5', 'Very Deep Scratch'), ('6', 'Bend In Structure')], copy=True, store=True)
    vehicle_status_in2 = fields.Selection(string='Vehicle Status In', selection=[], related='vehicle_status_in', readonly=True)
    vehicle_status_out = fields.Selection(string='Vehicle Status Out', selection=[('1', 'Excellent'), ('2', 'Good'), ('3', 'Simple Scratch'), ('4', 'Deep Scratch'), ('5', 'Very Deep Scratch'), ('6', 'Bend In Structure')], copy=True, store=True)
    vehicle_status_out2 = fields.Selection(string='Vehicle Status Out', selection=[], related='vehicle_status_out', readonly=True)
    vendor_id = fields.Many2one(comodel_name='res.partner', string='Vendor', copy=True,  store=True)
    website_message_ids = fields.One2many(comodel_name='mail.message', inverse_name='res_id', string='Website Messages', help="""Website communication history""", store=True)
    workshop_ids = fields.Many2many(comodel_name='maintenance.workshop', string='Workshop', copy=True, relation='maintenance_request_maintenance_workshop_rel', column1='maintenance_request_id', column2='maintenance_workshop_id', store=True)
    ywt_id = fields.Many2one(comodel_name='ywt.internal.stock.transfer', string='YWT', copy=True,  store=True)

    def cancel_request(self):
        pass

    def reset_to_draft(self):
        pass

    def confirm(self):
        pass

    def repaired(self):
        pass

    def request_spare_parts(self):
        pass

    def make_close(self):
        pass

    def create_bill(self):
        pass

    def create_vehicle_transfer(self):
        pass

    def action_view_delivery(self):
        pass

    def get_bills(self):
        pass

    def view_stock_transfer(self):
        pass
