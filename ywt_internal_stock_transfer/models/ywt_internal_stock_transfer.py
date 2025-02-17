from odoo import api, fields, models


class YwtInternalStockTransfer(models.Model):
    _name = 'ywt.internal.stock.transfer'
    _description = 'Ywt Internal Stock Transfer'
    
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    ac_in = fields.Selection(string='Ac In', selection=[('1', 'Excellent'), ('2', 'Good'), ('3', 'Weak'), ('4', 'Not Working')], copy=True, store=True)
    ac_out = fields.Selection(string='Ac Out', selection=[('1', 'Excellent'), ('2', 'Good'), ('3', 'Weak'), ('4', 'Not Working')], copy=True, store=True)
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
    bill_id = fields.Many2one(comodel_name='account.move', string='Bill', store=True)
    car_seats_in = fields.Selection(string='Car Seats In', selection=[('6', 'Clean'), ('7', 'Dirty')], copy=True, store=True)
    car_seats_out = fields.Selection(string='Car Seats Out', selection=[('6', 'Clean'), ('7', 'Dirty')], copy=True, store=True)
    checklist_km_in = fields.Float(string='k.m in', copy=True, store=True)
    checklist_km_out = fields.Float(string='k.m out', copy=True, store=True)
    checklist_user = fields.Many2one(comodel_name='res.users', string='Checklist User', related='write_uid', readonly=True)
    contact = fields.Selection(string='Contact', selection=[('vendor', 'Vendor'), ('employee', 'Employee')], copy=True, store=True)
    date_in = fields.Datetime(string='Date In', copy=True, store=True)
    date_out = fields.Datetime(string='Date Out', copy=True, store=True)
    destination = fields.Text(string='Destination', copy=True, store=True)
    deviation_ids = fields.One2many(comodel_name='ywt.internal.stock.transfer.line', inverse_name='internal_stock_transfer_id', string='Deviation Lines', store=True)
    deviation_states = fields.Selection(string='Status', selection=[('positive', 'Positive'), ('negative', 'Negative')], readonly=True)
    driver_id = fields.Many2one(comodel_name='vehicle.driver', string='Driver', store=True)
    employee_id = fields.Many2one(comodel_name='hr.employee', string='Employee', copy=True, store=True)
    fire_extinguisher_in = fields.Selection(string='Fire Extinguisher In', selection=[('8', 'Available'), ('9', 'Not Available')], copy=True, store=True)
    fire_extinguisher_out = fields.Selection(string='Fire Extinguisher Out', selection=[('8', 'Available'), ('9', 'Not Available')], copy=True, store=True)
    first_aid_kit_in = fields.Selection(string='First Aid Kit In', selection=[('8', 'Available'), ('9', 'Not Available')], copy=True, store=True)
    first_aid_kit_out = fields.Selection(string='First Aid Kit Out', selection=[('8', 'Available'), ('9', 'Not Available')], copy=True, store=True)
    from_location_id = fields.Many2one(comodel_name='stock.location', string='Source Location', readonly=True, store=True)
    from_warehouse_id = fields.Many2one(comodel_name='stock.warehouse', string='From Warehouse', copy=True, store=True)
    has_message = fields.Boolean(string='Has Message', readonly=True)
    image_in_1 = fields.Binary(string='Image 1', copy=True, store=True)
    image_in_2 = fields.Binary(string='Image 2', copy=True, store=True)
    image_in_3 = fields.Binary(string='Image 3', copy=True, store=True)
    image_in_4 = fields.Binary(string='Image 4', copy=True, store=True)
    image_in_5 = fields.Binary(string='Image 5', copy=True, store=True)
    image_in_6 = fields.Binary(string='Image 6', copy=True, store=True)
    image_in_7 = fields.Binary(string='Image 7', copy=True, store=True)
    image_in_8 = fields.Binary(string='Image 8', copy=True, store=True)
    image_out_1 = fields.Binary(string='Image 1', copy=True, store=True)
    image_out_2 = fields.Binary(string='Image 2', copy=True, store=True)
    image_out_3 = fields.Binary(string='Image 3', copy=True, store=True)
    image_out_4 = fields.Binary(string='Image 4', copy=True, store=True)
    image_out_5 = fields.Binary(string='Image 5', copy=True, store=True)
    image_out_6 = fields.Binary(string='Image 6', copy=True, store=True)
    image_out_7 = fields.Binary(string='Image 7', copy=True, store=True)
    image_out_8 = fields.Binary(string='Image 8', copy=True, store=True)
    internal_stock_transfer_line_ids = fields.One2many(comodel_name='ywt.internal.stock.transfer.line', inverse_name='internal_stock_transfer_id', string='Internal Stock Transfer Line', store=True)
    is_vehicle = fields.Boolean(string='Is Vehicle', copy=True, store=True)
    keys_in = fields.Selection(string='Keys In', selection=[('4', 'Working'), ('5', 'Not Working')], copy=True, store=True)
    keys_out = fields.Selection(string='Keys Out', selection=[('4', 'Working'), ('5', 'Not Working')], copy=True, store=True)
    maintenance_id = fields.Many2one(comodel_name='maintenance.request', string='Maintenance', copy=True, store=True)
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
    name = fields.Char(string='Stock Transfer Reference', required=True, store=True)
    note = fields.Text(string='Note', copy=True, store=True)
    picking_ids = fields.One2many(comodel_name='stock.picking', inverse_name='internal_stock_transfer_id', string='Pickings', readonly=True, store=True)
    plate_type_in = fields.Selection(string='Plate Type In', selection=[('1', 'Private'), ('3', 'Private Transport')], copy=True, store=True)
    plate_type_out = fields.Selection(string='Plate Type Out', selection=[('1', 'Private'), ('3', 'Private Transport')], copy=True, store=True)
    procurement_group_id = fields.Many2one(comodel_name='procurement.group', string='Procurement Group', readonly=True, ondelete='cascade', store=True)
    product_added = fields.Boolean(string='Product Added', store=True)
    radio_stereo_in = fields.Selection(string='Radio Stereo In', selection=[('1', 'Excellent'), ('2', 'Good'), ('3', 'Weak'), ('4', 'Not Working')], copy=True, store=True)
    radio_stereo_out = fields.Selection(string='Radio Stereo Out', selection=[('1', 'Excellent'), ('2', 'Good'), ('3', 'Weak'), ('4', 'Not Working')], copy=True, store=True)
    res_company_id = fields.Many2one(comodel_name='res.company', string='Company', copy=True, store=True)
    respo_employee = fields.Many2one(comodel_name='hr.employee', string='Respo Employee', copy=True, store=True)
    respo_vendor = fields.Many2one(comodel_name='res.partner', string='Respo Vendor', copy=True, store=True)
    safety_triangle_in = fields.Selection(string='Safety Triangle In', selection=[('8', 'Available'), ('9', 'Not Available')], copy=True, store=True)
    safety_triangle_out = fields.Selection(string='Safety Triangle Out', selection=[('8', 'Available'), ('9', 'Not Available')], copy=True, store=True)
    screen_in = fields.Selection(string='Screen In', selection=[('1', 'Excellent'), ('2', 'Good'), ('3', 'Weak'), ('4', 'Not Working')], copy=True, store=True)
    screen_out = fields.Selection(string='Screen Out', selection=[('1', 'Excellent'), ('2', 'Good'), ('3', 'Weak'), ('4', 'Not Working')], copy=True, store=True)
    product_ids = fields.Many2many(comodel_name='product.product', relation="product_rel", column1='ywt_id', column2='product_id', string='Product', readonly=True)
    second_product_ids = fields.Many2many(comodel_name='product.product', relation="second_product_rel", column1='ywt_id', column2='product_id', string='Second Product', readonly=True)
    spare_tire_tools_in = fields.Selection(string='Spare Tire Tools In', selection=[('8', 'Available'), ('9', 'Not Available')], copy=True, store=True)
    spare_tire_tools_out = fields.Selection(string='Spare Tire Tools Out', selection=[('8', 'Available'), ('9', 'Not Available')], copy=True, store=True)
    spare_tires_in = fields.Selection(string='Spare Tires In', selection=[('1', 'Excellent'), ('2', 'Good'), ('3', 'Weak')], copy=True, store=True)
    spare_tires_out = fields.Selection(string='Spare Tires Out', selection=[('1', 'Excellent'), ('2', 'Good'), ('3', 'Weak')], copy=True, store=True)
    speedometer_in = fields.Selection(string='Speedometer In', selection=[('4', 'Working'), ('5', 'Not Working')], copy=True, store=True)
    speedometer_out = fields.Selection(string='Speedometer Out', selection=[('4', 'Working'), ('5', 'Not Working')], copy=True, store=True)
    state = fields.Selection(string='State', selection=[('draft', 'Draft'), ('processed', 'Processed'), 
                                                        ('cancel', 'Cancel'), ('closed', 'Closed')], 
                                            index=True, store=True, default='draft')
    tires_in = fields.Selection(string='Tires In', selection=[('1', 'Excellent'), ('2', 'Good'), ('3', 'Weak')], copy=True, store=True)
    tires_out = fields.Selection(string='Tires Out', selection=[('1', 'Excellent'), ('2', 'Good'), ('3', 'Weak')], copy=True, store=True)
    to_location_id = fields.Many2one(comodel_name='stock.location', string='Destination Location', readonly=True, store=True)
    to_warehouse_id = fields.Many2one(comodel_name='stock.warehouse', string='To Warehouse', copy=True, store=True)
    transfer_number = fields.Char(string='Transfer Number', copy=True, store=True)
    transfer_type = fields.Selection(string='Transfer Type', selection=[('external', 'External'), ('internal', 'Internal'), ('custody', 'Custody'), ('task', 'Task'), ('return', 'Return'), ('maintenance', 'Maintenance')], copy=True, store=True)
    vehicle_id = fields.Many2one(comodel_name='fleet.vehicle', string='Vehicle', copy=True, store=True)
    vehicle_ids = fields.Many2many(comodel_name='fleet.vehicle', string='Vehicle', readonly=True)
    vehicle_status_in = fields.Selection(string='Vehicle Status In', selection=[('1', 'Excellent'), ('2', 'Good'), ('3', 'Simple Scratch'), ('4', 'Deep Scratch'), ('5', 'Very Deep Scratch'), ('6', 'Bend In Structure')], copy=True, store=True)
    vehicle_status_out = fields.Selection(string='Vehicle Status Out', selection=[('1', 'Excellent'), ('2', 'Good'), ('3', 'Simple Scratch'), ('4', 'Deep Scratch'), ('5', 'Very Deep Scratch'), ('6', 'Bend In Structure')], copy=True, store=True)
    vendor_id = fields.Many2one(comodel_name='res.partner', string='Vendor', store=True)
    website_message_ids = fields.One2many(comodel_name='mail.message', inverse_name='res_id', string='Website Messages', help="""Website communication history""", store=True)

    def action_button_stock_transfer_validate(self):
        pass

    def action_button_stock_transfer_cancel(self):
        pass

    def action_button_closed(self):
        pass

    def action_button_stock_transfer_draft(self):
        pass

    def action_view_stock_picking(self):
        pass

    def action_add_product(self):
        pass

    def action_clear(self):
        pass
    
        
class ProductProduct(models.Model):
    _inherit = 'product.product'

    product_rel = fields.Many2many(comodel_name='ywt.internal.stock.transfer', relation="product_ids", column1='product_id', column2='ywt_id', string='Product')
    second_product_rel = fields.Many2many(comodel_name='ywt.internal.stock.transfer', relation="second_product_ids", column1='product_id', column2='ywt_id', string='Second Product')
