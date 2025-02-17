from odoo import api, fields, models


class EmployeeChecklist(models.Model):
    _name = 'employee.checklist'
    _description = 'Employee Checklist'
    
    _inherit = ['mail.thread']
    
    document_type = fields.Selection(string='Checklist Type', selection=[('entry', 'Entry Process'), ('exit', 'Exit Process'), ('other', 'Other')], copy=True, required=True, store=True)
    has_message = fields.Boolean(string='Has Message', readonly=True)
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True)
    message_follower_ids = fields.One2many(comodel_name='mail.followers', inverse_name='emp_checklist_id', string='Followers', store=True)
    message_has_error = fields.Boolean(string='Message Delivery error', help="""If checked, some messages have a delivery error.""", readonly=True)
    message_has_error_counter = fields.Integer(string='Number of errors', help="""Number of messages with delivery error""", readonly=True)
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', help="""If checked, some messages have a delivery error.""", readonly=True)
    message_ids = fields.One2many(comodel_name='mail.message', inverse_name='emp_checklist_id', string='Messages', store=True)
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True)
    message_main_attachment_id = fields.Many2one(comodel_name='ir.attachment', string='Main Attachment', store=True)
    message_needaction = fields.Boolean(string='Action Needed', help="""If checked, new messages require your attention.""", readonly=True)
    message_needaction_counter = fields.Integer(string='Number of Actions', help="""Number of messages requiring action""", readonly=True)
    message_partner_ids = fields.Many2many(comodel_name='res.partner', string='Followers (Partners)')
    name = fields.Char(string='Document Name', required=True, store=True)
    website_message_ids = fields.One2many(comodel_name='mail.message', inverse_name='emp_checklist_id', string='Website Messages', help="""Website communication history""", store=True)
    

class MailFollowers(models.Model):
    _inherit = 'mail.followers'

    emp_checklist_id = fields.Many2one('employee.checklist', string='Employee Cheklist')
    
    
class MailMessage(models.Model):
    _inherit = 'mail.message'

    emp_checklist_id = fields.Many2one('employee.checklist', string='Employee Cheklist')