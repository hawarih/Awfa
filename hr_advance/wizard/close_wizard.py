from odoo import api, fields, models


class CloseWizard(models.TransientModel):
    _name = 'close.wizard'
    _description = 'Close Wizard'

    advance_id = fields.Many2one(comodel_name='advance.salary', string='Advance Salary', copy=True, store=True)
    close_date = fields.Date(string='Close Date', copy=True, required=True, store=True)
    company_id = fields.Many2one(comodel_name='res.company', string='Company', copy=True, ondelete='cascade', store=True)
    employee_id = fields.Many2one(comodel_name='hr.employee', string='Employee', related='advance_id.employee_id', readonly=True)
    is_at_line = fields.Boolean(string='Is At Line', copy=True, store=True)
    journal_id = fields.Many2one(comodel_name='account.journal', string='Journal', copy=True, required=True, ondelete='cascade', store=True)
    opened_line = fields.Integer(string='Opened Line', copy=True, store=True)
    remaining = fields.Float(string='Amount', copy=True, store=True)

    def action_close(self):
        pass
    
    def action_close_at_line(self):
        pass