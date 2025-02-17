from odoo import api, fields, models


class PettyCashAdj(models.Model):
    _name = 'petty.cash.adj'
    _description = 'Petty Cash Adj'

    account_move_id = fields.Many2one(comodel_name='account.move', string='Accounting Entry', readonly=True, store=True)
    adj_date = fields.Date(string='Adjustment Date', copy=True, store=True)
    amount = fields.Monetary(string='Amount', copy=True, store=True)
    currency_id = fields.Many2one(comodel_name='res.currency', string='Currency', copy=True, store=True)
    date = fields.Date(string='Payment Date', copy=True, store=True)
    employee_id = fields.Many2one(comodel_name='hr.employee', string='Employee To assign', related='petty_id.employee_id', readonly=True, store=True)
    has_message = fields.Boolean(string='Has Message', readonly=True)
    journal_id = fields.Many2one(comodel_name='account.journal', string='Petty Cash Journal', related='petty_id.journal_id', readonly=True, store=True)
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
    name = fields.Char(string='Reference', readonly=True, store=True)
    pay_journal_id = fields.Many2one(comodel_name='account.journal', string='Payment Journal', copy=True, store=True)
    petty_id = fields.Many2one(comodel_name='petty.cash', string='Petty Cash', copy=True, store=True)
    state = fields.Selection(string='State', selection=[('draft', 'Draft'), ('approved', 'Approved'), ('paid', 'Paid'), ('reconciled', 'Reconciled')], 
                             default='draft', store=True)
    type_id = fields.Many2one(comodel_name='petty.cash.type', string='Petty Cash Type', related='petty_id.type_id', readonly=True, store=True)
    website_message_ids = fields.One2many(comodel_name='mail.message', inverse_name='res_id', string='Website Messages', help="""Website communication history""", store=True)

    def action_approve(self):
            pass
        
    def action_draft(self):
            pass
        
    def action_register_petty_adj_payment(self):
            pass