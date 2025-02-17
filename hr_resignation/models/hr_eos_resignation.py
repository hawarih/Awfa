from odoo import api, fields, models


class HrEosResignation(models.Model):
    _name = 'hr.eos.resignation'
    _description = 'Hr Eos Resignation'
    
    _inherit = ['mail.thread']
    
    attachment_ids = fields.Many2many(comodel_name='ir.attachment', string='Attachments', copy=True, relation='resignation_attachments_rel', column1='res_id', column2='attach_id', store=True)
    company_id = fields.Many2one(comodel_name='res.company', string='Company', copy=True, ondelete='set null', store=True)
    duration_in_months = fields.Float(string='Duration In months', copy=True, store=True)
    employee_id = fields.Many2one(comodel_name='hr.employee', string='Employee Name', help="""Name of the employee for whom the request is creating""", related='resignation_request_id.employee_id', readonly=True, store=True)
    eos_reward = fields.Float(string='EOS Reward', copy=True, store=True)
    excluded_period_days = fields.Float(string='Excluded Service Period(Days)', copy=True, store=True)
    has_message = fields.Boolean(string='Has Message', readonly=True)
    hiring_date = fields.Date(string='Hiring Date', copy=True, store=True)
    journal_id = fields.Many2one(comodel_name='account.journal', string='Journal', copy=True, ondelete='set null', store=True)
    last_working_date = fields.Date(string='Last Working Day', copy=True, store=True)
    leave_balance = fields.Float(string='Leave Balance', copy=True, store=True)
    leave_balance_compensation = fields.Float(string='Leave Balance Compensation', copy=True, store=True)
    loan_count = fields.Integer(string='Loan Count', copy=True, store=True)
    loan_installed = fields.Boolean(string='Loan Installed', readonly=True)
    loan_remaining_amount = fields.Float(string='Loan Remaining Amount', readonly=True)
    max_leave_compensation = fields.Float(string='Max. Leave Compensation', copy=True, store=True)
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
    move_id = fields.Many2one(comodel_name='account.move', string='Entry.*', copy=True, ondelete='set null', store=True)
    notes = fields.Text(string='Employee Comments', copy=True, store=True)
    other_allowed_amount = fields.Float(string='Other Allowed Amount', copy=True, store=True)
    other_deduction_amount = fields.Float(string='Other Deduction Amount', copy=True, store=True)
    payslip_id = fields.Many2one(comodel_name='hr.payslip', string='Payslip', copy=True, ondelete='set null', store=True)
    process_type = fields.Selection(string='Processing Type', selection=[('payroll', 'Payroll')], copy=True, store=True)
    reason_id = fields.Many2one(comodel_name='hr.resignation.reason', string='Resignation Reason', copy=True, ondelete='set null', store=True)
    refuse_reason = fields.Char(string='Refuse Reason', copy=True, translate=True, store=True)
    request_date = fields.Date(string='Request Date', copy=True, store=True)
    resignation_request_id = fields.Many2one(comodel_name='hr.resignation', string='Resignation Request', copy=True, required=True, ondelete='restrict', store=True)
    service_period_day = fields.Float(string='Service Period(Days)', copy=True, store=True)
    service_period_month = fields.Float(string='Service Period(Months)', copy=True, store=True)
    service_period_year = fields.Float(string='Service Period(Years)', copy=True, store=True)
    settlement_remaining_amount = fields.Float(string='Settlement Remaining Amount', readonly=True)
    state = fields.Selection(string='Status', selection=[('draft', 'جديد'), ('confirm', 'Confirm'), ('approve', 'Approve'), 
                                                         ('post', 'Posted'), ('paid', 'Paid'), ('refuse', 'Refused'), ('cancel', 'Cancelled')], 
                                                store=True, default='draft')
    ticket_reward = fields.Float(string='Ticket Reward', copy=True, store=True)
    total_eos_reward = fields.Float(string='Total EOS Reward', readonly=True)
    website_message_ids = fields.One2many(comodel_name='mail.message', inverse_name='res_id', string='Website Messages', help="""Website communication history""", store=True)

    def compute_sheet(self):
        pass

    def button_confirm(self):
        pass

    def button_refuse(self):
        pass

    def button_approve(self):
        pass

    def button_refuse(self):
        pass

    def create_payslip(self):
        pass

    def button_cancel(self):
        pass

    def button_refuse(self):
        pass

    def button_refuse(self):
        pass

    def button_refuse(self):
        pass

    def button_draft(self):
        pass
