from odoo import api, fields, models


class StockInventory(models.Model):
    _name = 'stock.inventory'
    _description = 'Stock Inventory'

    accounting_date = fields.Date(string='Accounting Date', help="""Date at which the accounting entries will be created in case of automated inventory valuation. If empty, the inventory date will be used.""", copy=True, store=True)
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
    company_id = fields.Many2one(comodel_name='res.company', string='Company', copy=True, required=True, readonly=True, index=True, ondelete='restrict', store=True)
    date = fields.Datetime(string='Inventory Date', help="""If the stock adjustment is not validated, date at which the theoritical quantities have been checked.
If the stock adjustment is validated, date at which the stock adjustment has been validated.""", copy=True, required=True, readonly=True, store=True)
    exhausted = fields.Boolean(string='Include Exhausted Products', help="""Include also products with quantity of 0""", copy=True, readonly=True, store=True)
    has_account_moves = fields.Boolean(string='Has Account Moves', readonly=True)
    has_message = fields.Boolean(string='Has Message', readonly=True)
    line_ids = fields.One2many(comodel_name='stock.inventory.line', inverse_name='inventory_id', string='Inventories', store=True)
    location_ids = fields.Many2many(comodel_name='stock.location', string='Locations', copy=True, readonly=True, relation='stock_inventory_stock_location_rel', column1='stock_inventory_id', column2='stock_location_id', store=True)
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
    move_ids = fields.One2many(comodel_name='stock.move', inverse_name='inventory_id', string='Created Moves', store=True)
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True)
    name = fields.Char(string='Inventory Reference', copy=True, required=True, readonly=True, store=True)
    prefill_counted_quantity = fields.Selection(string='Counted Quantities', help="""Allows to start with a pre-filled counted quantity for each lines or with all counted quantities set to zero.""", selection=[('zero', 'Default to zero'), ('on_hand', 'Default to On Hand')], copy=True, required=True, store=True)
    product_ids = fields.Many2many(comodel_name='product.product', string='Products', help="""Specify Products to focus your inventory on particular Products.""", copy=True, readonly=True, relation='product_product_stock_inventory_rel', column1='stock_inventory_id', column2='product_product_id', store=True)
    start_empty = fields.Boolean(string='Empty Inventory', help="""Allows to start with an empty inventory.""", copy=True, store=True)
    state = fields.Selection(string='Status', selection=[('draft', 'Draft'), ('cancel', 'Cancelled'), ('confirm', 'In Progress'), 
                                                         ('waiting', 'Waiting Approval'), ('approved', 'Approved'), 
                                                         ('done', 'Validated')], readonly=True, index=True,
                                                            default='draft')
    website_message_ids = fields.One2many(comodel_name='mail.message', inverse_name='res_id', string='Website Messages', help="""Website communication history""", store=True)

    def action_start(self):
        pass

    def action_open_inventory_lines(self):
        pass

    def action_validate(self):
        pass

    def action_validate(self):
        pass

    def action_confirm(self):
        pass

    def action_approve(self):
        pass

    def action_print(self):
        pass

    def action_cancel_draft(self):
        pass

    def action_cancel_draft(self):
        pass

    def action_view_related_move_lines(self):
        pass

    def action_view_inventory_lines(self):
        pass

    def action_get_account_moves(self):
        pass
