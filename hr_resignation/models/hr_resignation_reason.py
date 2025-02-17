from odoo import api, fields, models


class HrResignationReason(models.Model):
    _name = 'hr.resignation.reason'
    _description = 'Hr Resignation Reason'

    _inherit = ['mail.thread', 'mail.activity.mixin']

    code = fields.Char(string='Code', store=True)
    company_id = fields.Many2one(comodel_name='res.company', string='Company', copy=True, ondelete='set null', store=True)
    employee_rule_ids = fields.Many2many(comodel_name='hr.salary.rule', string='Rules', copy=True, relation='employee_rule_salary_rel', column1='employee_res_id', column2='employee_rule_id', store=True)
    has_message = fields.Boolean(string='Has Message', readonly=True)
    leave_provision_month_days = fields.Integer(string='Calculate Compensation Months Days', help="""Number of days per month while calculation leave compensation""", copy=True, store=True)
    leave_rule_ids = fields.Many2many(comodel_name='hr.salary.rule', string='Leave Compensation Elements', copy=True, relation='leave_compensation_salary_rule_rel', column1='res_id', column2='rule_id', store=True)
    max_leave_compensation = fields.Float(string='Max. Leave Accruals Compensation', copy=True, store=True)
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
    name = fields.Char(string='Reason Name', copy=True, required=True, translate=True, store=True)
    resignation_by_employee = fields.Boolean(string='Resignation by Employee', copy=True, store=True)
    rule_ids = fields.One2many(comodel_name='hr.resignation.reason.rule', inverse_name='reason_id', string='Rules', copy=True, store=True)
    website_message_ids = fields.One2many(comodel_name='mail.message', inverse_name='res_id', string='Website Messages', help="""Website communication history""", store=True)
